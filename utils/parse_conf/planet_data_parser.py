import json
from data_fetcher import fetch_data_from_url
from conf import settings

PLANETS_URL = settings.url.get("planets")
PLANET_STATS_URL = settings.url.get("planet_stats")

