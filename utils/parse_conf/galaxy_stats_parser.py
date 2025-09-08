# Stats parser
def parse_galaxy_stats(data):

    parsed_stats = []

    if not isinstance (data, dict):
        print(f"Error: Expected a dictionary for war-specific details, but received {type(data)}")
        return None
    
    try:
        
        # Store all stats dictionary
        galaxy_stats_list = data.get("galaxy_stats", {})
        parsed_stats["galaxy_stats"] = galaxy_stats_list

        return parsed_stats

    except (AttributeError, TypeError) as e:
        print(f"Error processing war details: {e}")
        return None
