import json
import requests
from . import api_endpoints

def parse_war_details(data):

    parsed_orders = []

    if not isinstance (data, dict):
        print(f"Error: Expected a list of war-specific details, but received {type(data)}")
        return None
    
    try:

        for stats in data:
            war_start_date = stats.get("started", {})
            war_current_date = stats.get("now", {})

            stats_dict = stats.get("statistics")
            if isinstance(stats_dict, dict):
                missions_won = stats_dict.get("missionsWon")
                missions_lost = stats_dict.get("missionsLost")
                mission_time = stats_dict.get("missionTime")
                terminid_kills = stats_dict.get("terminidKills")
                automoton_kills = stats_dict.get("automotonKills")
                illuminate_kills = stats_dict.get("illuminateKills")
                bullets_fired = stats_dict.get("bulletsFired")
                bullets_hit = stats_dict.get("bulletsHit")
                time_played = stats_dict.get("timePlayed")
