from fastapi import FastAPI
from app.api.routers import router as profile_router
from datetime import datetime


app = FastAPI(
    title="Clean Profile API",
    description="Profile endpoint with separated external API integration.",
    json_encoders={
        datetime: lambda dt: dt.isoformat(),
    },
    json_dumps_params={"indent": 4}
)


app.include_router(
    profile_router,
    prefix="/api" 
)