import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class WeatherService:
    BASE_URL = "https://api.weatherapi.com/v1/current.json"

    async def get_current_weather(self, city: str) -> dict:
        api_key = os.getenv("WEATHERAPI_KEY")
        if not api_key:
            raise RuntimeError("No se configuró WEATHERAPI_KEY en las variables de entorno.")
        if not city:
            raise ValueError("Debes ingresar una ciudad.")

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    self.BASE_URL,
                    params={"key": api_key, "q": city, "lang": "es"},
                )
            data = response.json()
        except httpx.RequestError as exc:
            raise RuntimeError(f"No se pudo conectar con WeatherAPI: {exc}") from exc

        if response.status_code != 200:
            message = data.get("error", {}).get("message", "WeatherAPI devolvió un error.")
            raise RuntimeError(message)

        return {
            "city": data["location"]["name"],
            "country": data["location"]["country"],
            "temperature": round(data["current"]["temp_c"]),
            "feelsLike": round(data["current"]["feelslike_c"]),
            "humidity": data["current"]["humidity"],
            "wind": data["current"]["wind_kph"],
            "description": data["current"]["condition"]["text"],
            "icon": f'https:{data["current"]["condition"]["icon"]}',
            "source": "WeatherAPI",
        }
