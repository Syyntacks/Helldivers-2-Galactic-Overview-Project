import json
import datetime
from . import api_endpoints
from . import datetime_converter


# https://api.helldivers2.dev/api/v1/war


def parse_war_details(data):

    parsed_stats = {}

    if not isinstance (data, dict):
        print(f"Error: Expected a dictionary for war-specific details, but received {type(data)}")
        return None
    
    try:
        """
            Key detail here is that we use the empty list above (parsed_stats) 
            to identify and list the required statistics in an easily readable format
            rather than defining each value accordingly.
        """
        current_datetime = datetime.datetime.now(datetime.timezone.utc)

        # WarID
        parsed_stats["warId"] = data.get("warId")

        # Timestamp stats
        parsed_stats["start_time"] = data.get("started")
        parsed_stats["end_time"] = data.get("ended")

        current_time_iso = current_datetime.isoformat(timespec="seconds")
        parsed_stats["current_time"] = current_time_iso

        # Store all stats dictionary
        statistics_data = data.get("statistics", {})
        parsed_stats["overall_war_stats"] = statistics_data
        
        parsed_stats["client_version"] = data.get("clientVersion")
        
        print("\nSuccesfully parsed Galactic War details.")
        return parsed_stats

    except (AttributeError, TypeError) as e:
        print(f"Error processing war details: {e}")
        return None
