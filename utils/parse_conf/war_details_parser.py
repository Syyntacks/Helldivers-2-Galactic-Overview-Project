import json
import datetime
from . import api_endpoints

# https://api.helldivers2.dev/api/v1/war
def parse_iso_timestamp(iso_string):

    if iso_string is None:
        return None
    try:
        dt_object_utc = datetime.datetime.fromisoformat(iso_string.replace('Z', "+00:00"))
        return dt_object_utc.strftime("%Y-%M-%D %H:%M:%S UTC")
    except (ValueError, TypeError):
        return "\nInvalid Timestamp format"
    except Exception as e:
        return f"An unexpected error occurred: {e}"



def parse_war_details(data):

    parsed_stats = {}

    if not isinstance (data, dict):
        print(f"Error: Expected a dictionary for war-specific details, but received {type(data)}")
        return None
    
    try:
        """
            Key detail here is that we use the empty list above (parsed_stats) 
            is to identify and list the required statistics in an easily readable format
            rather than defining each value accordingly.
        """

        # WarID
        parsed_stats["warId"] = data.get("warId")

        # Timestamp stats
        parsed_stats["start_time"] = parse_iso_timestamp(data.get("started"))
        parsed_stats["end_time"] = parse_iso_timestamp(data.get("ended"))
        parsed_stats["current_time"] = parse_iso_timestamp(data.get("now"))

        # Store all stats dictionary
        statistics_data = data.get("statistics", {})
        parsed_stats["overall_war_stats"] = statistics_data
        
        parsed_stats["client_version"] = data.get("clientVersion")
        
        print("\nSuccesfully parsed Galactic War details.")
        return parsed_stats

    except (AttributeError, TypeError) as e:
        print(f"Error processing war details: {e}")
        return None
