import json
import requests
from . import api_endpoints

# https://api.helldivers2.dev/api/v1/war
def parse_war_details(data):

    parsed_stats = []

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
                deaths = stats_dict.get("deaths")
                revives = stats_dict.get("revives")
                friendly_kills = stats_dict.get("friendlies")
                mission_success_rate = stats_dict.get("missionSuccessRate")
                accuracy = stats_dict.get("accuracy")
                current_player_count = stats_dict.get("playerCount")

            if war_start_date and war_current_date:
                war_stats = {
                    "missionsWon": missions_won,
                    "missionsLost": missions_lost,
                    "missionTime": mission_time,
                    "terminidKills": terminid_kills,
                    "automotonKills": automoton_kills,
                    "illuminateKills": illuminate_kills,
                    "bulletsFired": bullets_fired,
                    "bulletsHit": bullets_hit,
                    "timePlayed": time_played,
                    "deaths": deaths,
                    "revives": revives,
                    "friendlies": friendly_kills,
                    "missionSuccessRate": mission_success_rate,
                    "accuracy": accuracy,
                    "playerCount": current_player_count
                }
            

    except (AttributeError, TypeError) as e:
        print(f"Error processing stats: {e}")
        return None
