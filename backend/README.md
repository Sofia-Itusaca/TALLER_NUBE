# TALLER_NUBE - Backend

Backend FastAPI para consultar WeatherAPI sin exponer la API Key en el frontend.

## Configuración

Desde `backend`:

```powershell
Copy-Item .env.example .env
```

Edita `.env`:

```env
WEATHERAPI_KEY=TU_CLAVE_REAL
```

No subas `.env` a GitHub.

## Ejecutar

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Swagger:
`http://127.0.0.1:8000/docs`

Health:
`http://127.0.0.1:8000/health`

Clima:
`http://127.0.0.1:8000/api/weather?city=Lima`

El frontend debe consultar el backend, no WeatherAPI directamente.
