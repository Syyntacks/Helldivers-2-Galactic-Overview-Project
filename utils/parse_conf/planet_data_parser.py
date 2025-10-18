from typing import Dict, Any, Union, List
from utils.parse_conf.data_fetcher import fetch_data_from_url
from conf import settings

PLANETS_URL: str = settings.urls.get("planets")
PLANET_DETAILS_URL: str = settings.urls.get("planet_stats")
PLANET_STATUS_URL: str = settings.urls.get("status")

class PlanetParser():
    """
        Handles all functions regarding all planets
        on the Galactic Map.
        \n3 sources combined.
    """

    def __init__(self):
        self.combined_data: Dict[int, Dict[str, Any]] = {} # Return for better understanding
        self._fetch_and_combine()
    

    def _fetch_and_combine(self):
        # Creates one dictionary from API endpoints
        planets_data = fetch_data_from_url(PLANETS_URL)
        details_data = fetch_data_from_url(PLANET_DETAILS_URL)
        status_data = fetch_data_from_url(PLANET_STATUS_URL)

        if not planets_data or not details_data or not status_data:
            print("\nCould not combine data due to fetching errors.")
            return
        
        # Dictionary Comprehension --> for further reference
        planets_dict = {int(key): value for key, value in planets_data.items() if key.isdigit()}
        details_dict = {int(key): value for key, value in details_data.items() if key.isdigit()}
        status_planets_dict = {int(key): value for key, value in status_data.items() if key.isdigit()}

        # Combine data
        for index, planet_detail in planets_dict.items():
            details = details_dict.get(index, {}) # Get planet details
            status = status_planets_dict.get(index, {}) # Get stats of planet

            # Labelling
            self.combined_data[index] = {
                # planet_detail for planet specifics!
                'index': index,
                'name': planet_detail.get('name', 'Unknown'),
                'sector': planet_detail.get('sector', 'Unknown Sector'),
                'type': planet_detail.get('type', 'Unknown Type'),
                'biome': planet_detail.get('biome', {}).get('name', 'Unknown Biome'),
                'description': planet_detail.get('biome', {}).get('description', 'No Description'),
                'environName': [env.get('name') for env in planet_detail.get('environmentals', [])],
                'environDesc': [env.get('description') for env in planet_detail.get('environmentals', [])],
                'weatherEffects': planet_detail.get('weather_effects'),
                
                # status
                'players': status.get('players', 0),
                'owner': status.get('owner', 'N/A'),

                # planet_stats/planets_stats
                "missionsWon": "Missions Won",
                "missionsLost": "Missions Lost",
                "missionTime": "Total Mission Time (ms)",
                "bugKills": "Terminid Kills",
                "automatonKills": "Automaton Kills",
                "illuminateKills": "Illuminate Kills",
                "bulletsFired": "Total Bullets Fired",
                "bulletsHit": "Total Bullets Hit",
                "timePlayed": "Total Time Played (ms)",
                "deaths": "Total Deaths",
                "friendlies": "Friendly Kills",
                "missionSuccessRate": "Mission Success Rate",

            }


    def get_all_planets(self):
        return self.combined_data


    def get_planet_by_name(self, planet_name: str):
        for planet in self.combined_data.values():
            if planet.get('name', '').lower() == planet_name.lower():
                return planet
        return None
    

    def get_planet_name_by_id(self, planet_id: int) -> str:
        if planet_id is None:
            return "N/A"
            
        planet_info = self.combined_data.get(planet_id)
        if planet_info:
            return planet_info.get('name', 'Unknown Planet')
        return "Unknown Planet ID"