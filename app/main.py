from fastapi import FastAPI
from app.api.routers import router as profile_router
from datetime import datetime


app = FastAPI(
    title="Clean Profile API",
    description="Profile endpoint with separated external API integration.",
    json_encoders={
        datetime: lambda dt: dt.isoformat(), # Optional: ensures datetime is formatted
    },
    json_dumps_params={"indent": 4} # <-- THIS FORCES PRETTY-PRINTING
)


app.include_router(
    profile_router,
    prefix="/api" # Use an API version prefix
)

# Note: httpx client management is handled by the dependency injection 
# in the service layer, making this file very clean.

# To run: uvicorn app.main:app --reload