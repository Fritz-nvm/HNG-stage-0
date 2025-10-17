from fastapi import FastAPI
from app.api.routers import profile

app = FastAPI(
    title="Clean Profile API",
    description="Profile endpoint with separated external API integration.",
)

app.include_router(
    profile.router,
    prefix="/api/v1" # Use an API version prefix
)

# Note: httpx client management is handled by the dependency injection 
# in the service layer, making this file very clean.

# To run: uvicorn app.main:app --reload