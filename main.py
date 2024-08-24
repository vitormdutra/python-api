import uvicorn
from fastapi import FastAPI, HTTPException, Query, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import requests
import logging
from cachetools import cached, TTLCache
import os


logging.basicConfig(level=logging.INFO)
cache = TTLCache(maxsize=100, ttl=300)

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

app = FastAPI()

origins = [
    "http://localhost:3000",  # URL do frontend se estiver em outra origem
    "http://localhost:8000",  # Para acessar via mesma origem
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@cached(cache)
def fetch_weather_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching weather data: {e}")
        return None

@app.get("/weather", summary="Get weather information", description="Retrieve weather data for a specific city and country.")
def get_weather(city: str = Query(..., description="Name of the city"), country: str = Query(..., description="Country code (e.g., 'BR' for Brazil)")):
    logging.info(f"Receiving request for weather forecast for {city}, {country}")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={OPENWEATHERMAP_API_KEY}&units=metric"

    weather = fetch_weather_data(url)
    if not weather:
        logging.error(f"Failed to fetch weather data for {city}, {country}")
        raise HTTPException(status_code=502, detail="Failed to fetch weather data")

    logging.info(f"Weather data successfully retrieved for {city}, {country}")
    return JSONResponse(content=weather)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
