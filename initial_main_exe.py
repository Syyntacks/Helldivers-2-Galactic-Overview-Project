import time
import requests
import json
import os


'''
    Personal project accessing Helldiver's 2 metadata to 
    then display in a personalized and intuitive GUI.
'''



"""
    FUNCTIONS
"""

# Fetch API data
def fetch_hd2_api_data(endpoint_url):

    # Must identify self with custom headers
    personal_headers = {
        "X-Super-Client": "Helldivers2StatusMonitorProject",
        "X-Super-Contact": "adamaso.ad8@gmail.com"
    }

    try:
        response = requests.get(endpoint_url, headers=personal_headers)
        response.raise_for_status() # Raises an exception if HTTP error encountered
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:   # Define the exception as e
        print(f"Error fetching data: {e}") # Return the occurring exception
        return None


# Save JSON info to file
def save_json_to_file(data, filename):
    try:
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4) 
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")
        


# Galactic-related Variables
data_export_folder = "data_exports"
os.makedirs(data_export_folder, exist_ok=True) # If folder doesn't exist, create it


# API Data Endpoints
# RAW
api_data_endpoints = {}
current_war_id_ep = "https://api.helldivers2.dev/raw/api/WarSeason/current/WarID", # ID of current war
war_status_snapshot_ep = "https://api.helldivers2.dev/raw/api/WarSeason/801/Status", # Endpoint for Galactic War Status
war_info_ep = "https://api.helldivers2.dev/raw/api/WarSeason/801/WarInfo",  # Current war's info
war_summary_ep = "https://api.helldivers2.dev/raw/api/Stats/war/801/summary", # Endpoint for summarized static data
se_news_feed_ep = "https://api.helldivers2.dev/raw/api/NewsFeed/801",   # Super Earth news feed
active_war_assignments_ep = "https://api.helldivers2.dev/raw/api/v2/Assignment/War/801",    # Active Assignments (e.g., Major Orders)
news_space_station_ep = "https://api.helldivers2.dev/raw/api/v2/SpaceStation/War/801/{index}",  # Fetches specified news SpaceStation

#V1
overall_war_stats_ep = "https://api.helldivers2.dev/api/v1/war",                    # Overarching war stats
available_major_orders_ep = "https://api.helldivers2.dev/api/v1/assignments",       # Fetches a list of all available Major Orders
indexed_major_order_ep = "https://api.helldivers2.dev/api/v1/assignments/{index}",  # Fetches specific Major Order
overall_campaigns_ep = "https://api.helldivers2.dev/api/v1/campaigns",              # Fetches all available campaign's info
specific_campaign_ep = "https://api.helldivers2.dev/api/v1/campaigns/{index}",      # Fetches specific indexed campaign's info
high_command_dispatch_ep = "https://api.helldivers2.dev/api/v1/dispatches",         # Fetches any avilable Dispatch info from High Command
specific_dispatch_ep = "https://api.helldivers2.dev/api/v1/dispatches/{index}",     # Fetches specific HC Dispatch
planets_info_ep = "https://api.helldivers2.dev/api/v1/planets",                     # Fetches all aggregated planet info
specific_planet_info_ep = "https://api.helldivers2.dev/api/v1/planets/{index}",     # Fetches specific planet info
active_planet_events_ep = "https://api.helldivers2.dev/api/v1/planet-events",       # Fetches all planets with Active Events
steam_newsfeed_ep = "https://api.helldivers2.dev/api/v1/steam",                     # Fetches Steam's HD2 newsfeed
specific_steam_newsfeed_ep = "https://api.helldivers2.dev/api/v1/steam/{grid}",     # Fetches specific Steam newsfeed item

#V2
released_dispatches_ep = "https://api.helldivers2.dev/api/v2/dispatches",           # Fetches all released dispatches since game release
specific_released_dispatch_ep = "https://api.helldivers2.dev/api/v2/dispatches/{index}",   # Fetches all released dispatches since game release
dss_location_info_ep = "https://api.helldivers2.dev/api/v2/space-stations",         # Fetches DSS's location's info
specific_dss_location_ep = "https://api.helldivers2.dev/api/v2/space-stations/{index}",    # Fetches specific location's info (DSS-related?)



hd2_galactic_war_status_data = fetch_hd2_api_data() 