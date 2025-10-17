from fastapi import APIRouter, Depends
from app.infastructure.models import Response, User
from app.application.service import CatFactService
from datetime import datetime

router = APIRouter(tags=["Profile"])

@router.get("/me", response_model=Response)
async def get_my_profile(
    cat_fact_service: CatFactService = Depends()
):
    """
    Returns static profile information combined with a dynamic cat fact
    fetched via the service layer.
    """
    # 1. Fetch the dynamic data via the service
    dynamic_fact = await cat_fact_service.fetch_random_fact()
    
    # 2. Define the static profile data
    user_data = User(
        name="Fritz Akam",
        email ="fritzimpah@gmail.com",
        stack ="Python, FastAPI",

    )
    
    # 3. Combine and return
    return Response(
        status="success", # Example status
        user=user_data,
        timestamp=datetime.now().isoformat(), # You need to import datetime
        cat_fact=dynamic_fact,
    )