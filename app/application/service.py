# app/services/cat_fact_service.py
import httpx
from fastapi import HTTPException, Depends
from app.config import settings
from app.infastructure.external import CatFact


# Dependency: Async HTTP client setup
# We use a dependency to manage the client's lifecycle
def get_http_client():
    """Initializes and yields an httpx.AsyncClient."""
    client = httpx.AsyncClient(timeout=10)  # Set a reasonable timeout
    try:
        yield client
    finally:
        # Note: In a larger app, you might pass the client to the router/service and close it on shutdown.
        # For simple dependency injection, the client is usually defined globally or managed by startup/shutdown events.
        pass


class CatFactService:
    def __init__(self, client: httpx.AsyncClient = Depends(get_http_client)):
        self.client = client
        self.api_url = settings.CAT_FACT_API_URL

    async def fetch_random_fact(self) -> str:
        """Fetches a single cat fact, handles errors, and returns just the fact string."""
        try:
            # 1. Make the external API call
            response = await self.client.get(self.api_url)
            response.raise_for_status()  # Raises HTTPStatusError for 4xx/5xx responses

            # 2. Validate/parse the external response using Pydantic
            fact_data = CatFact.model_validate(response.json())

            # 3. Return the specific piece of data needed by the caller
            return fact_data.fact

        except httpx.HTTPStatusError as e:
            # Re-raise external errors as a generic 500
            raise HTTPException(
                status_code=500,
                detail=f"External Cat Fact API returned status {e.response.status_code}",
            )
        except httpx.RequestError:
            # Re-raise network/connection errors as a 503
            raise HTTPException(
                status_code=503, detail="Cannot connect to external Cat Fact API."
            )
        except Exception:
            # Catch all other unexpected errors (e.g., Pydantic parsing)
            raise HTTPException(
                status_code=500, detail="Error processing cat fact data."
            )
