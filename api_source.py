from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.parse_conf.planet_data_parser import PlanetParser
from utils.parse_conf.major_order_parser import parse_major_order_data
from utils.parse_conf.galaxy_stats_parser import parse_galaxy_stats
from utils.parse_conf.data_fetcher import fetch_data_from_url
from conf import settings

# Initiation for FastAPI app
app = FastAPI()

# Defining which origins are allowed to make requests 
# Works with the CORS FastAPI
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "*" # Allows everything for testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # All methods (GET, POST, etc.)
    allow_headers=["*"]  # All headers
)

"""
    We define endpoints below for users to access. Subject to change.
"""

@app.get("/")
def get_root():
    print("If you are reading this message, the Helldivers 2 API is running." \
    "\nGo to /api/planets, /api/major_orders, or /api/galaxy_stats to access data.") 

# All planet data combined
@app.get("/api/planets") 
def get_all_planets():
    print("Request received for all planet data...")
    planet_handler = PlanetParser()
    return planet_handler.get_all_planets()

# Specific planet data
@app.get("/api/planets/{planet_name}")
def get_single_planet(planet_name: str):
    print("Request received for planet {planet_name}...")
    planet_handler = PlanetParser()
    planet = planet_handler.get_planet_by_name(planet_name)
    return planet if planet else {"error": "Planet was not found"}

# Major order data
@app.get("/api/major_orders")
def get_major_orders():
    print("Request received for major orders...")
    major_order_url = settings.urls.get("major_order")
    raw_data = fetch_data_from_url(major_order_url)
    if raw_data:
        parsed_orders = parse_major_order_data(raw_data)
        return parsed_orders
    return {"error": "Failed to fetch major order data"}

# Galaxy stats
@app.get("/api/galaxy_stats")
def get_galaxy_stats():
    print("Request received for galaxy stats...")
    galaxy_stats_url = settings.urls.get("planet_stats")
    raw_data = fetch_data_from_url(galaxy_stats_url)
    if raw_data:
        galaxy_stats = parse_galaxy_stats(raw_data) # returns a list
        return galaxy_stats
    return {"error": "Failed to fetch galaxy stats"}