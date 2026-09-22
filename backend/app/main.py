from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.weather import router as weather_router

app = FastAPI(title="TALLER_NUBE Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(weather_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok", "service": "taller-nube-backend"}
