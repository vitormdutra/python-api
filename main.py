from fastapi import FastAPI, HTTPException, Query, Header
from fastapi.responses import JSONResponse
import requests
import uvicorn
import logging
from cachetools import cached, TTLCache

logging.basicConfig(level=logging.INFO)
cache = TTLCache(maxsize=100, ttl=300)
OPENWEATHERMAP_API_KEY = "Information goes here"

app = FastAPI()

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
def get_weather(api_key: str = Header(...), city: str = Query(..., description="Name of the city"), country: str = Query(..., description="Country code (e.g., 'BR' for Brazil)")):
    if api_key != "Define a key for API":
        raise HTTPException(status_code=403, detail="Invalid API Key")
    logging.info(f"Receiving request for weather forecast for {city}, {country}")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={OPENWEATHERMAP_API_KEY}&units=metric"

    weather = fetch_weather_data(url)
    if not weather:
        logging.error(f"Failed to fetch weather data for {city}, {country}")
        raise HTTPException(status_code=502, detail="Failed to fetch weather data")

    logging.info(f"Weather data successfully retrieved for {city}, {country}")
    return JSONResponse(content=weather)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)