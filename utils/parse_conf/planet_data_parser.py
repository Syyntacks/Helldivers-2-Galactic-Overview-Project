import json
from typing import Dict, Any, Union, List
from data_fetcher import fetch_data_from_url
from conf import settings

PLANETS_URL: str = settings.url.get("planets")
PLANET_DETAILS_URL: str = settings.url.get("planet_stats")
PLANET_STATS_URL: str = settings.url.get("status")

class PlanetParser:
    """
        Handles all functions regarding all planets
        on the Galactic Map.
    """

    def __init__(self):
        self.combined_data: Dict[int, Dict[str, Any]] = {} # Return for better understanding
        self._fetch_and_combine()
    

    def _fetch_and_combine(self):
        # Creates one dictionary from both API endpoints
        planets_data = fetch_data_from_url(PLANETS_URL)
        details_data = fetch_data_from_url(PLANET_DETAILS_URL)
        stats_data = fetch_data_from_url(PLANET_STATS_URL)

        if not planets_data or not details_data or not stats_data:
            print("\nCould not combine data due to fetching errors.")
            return
        
        # Dictionary Comprehension 
        planets_dict = {planet['index']: planet for planet in planets_data}
        details_dict = {detail['planetIndex']: detail for detail in details_data}
        stats_dict = {stat['statIndex']: stat for stat in stats_data}

        # Combine data
        for index, planet_detail in planets_dict.items():
            details = details_dict.get(index, {}) # Get planet details
            stats = stats_dict.get(index, {}) # Get stats of planet

            # Labelling
            self.combined_data[index] = {
                # Planet Details
                'index': index,
                'name': planet_detail.get('name', 'Unknown'),
                'sector': planet_detail.get('sector', 'Unknown Sector'),
                'type': planet_detail.get('type', 'Unknown Type'),
                'biome': planet_detail.get('biome', {}).get('name', 'Unknown Biome'),
                'description': planet_detail.get('biome', {}).get('description', 'No Description'),
                'environName': [env.get('name') for env in planet_detail.get('environmentals', [])],
                'environDesc': [env.get('description') for env in planet_detail.get('environmentals', [])],
                'weatherEffects': planet_detail.get('weather_effects'),
                
                # Stats
                'players': stats
            }