from fastapi import APIRouter, HTTPException, Query
from app.services.weather_service import WeatherService

router = APIRouter(tags=["weather"])
service = WeatherService()

@router.get("/weather")
async def get_weather(city: str = Query(..., min_length=1)):
    try:
        return await service.get_current_weather(city.strip())
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
