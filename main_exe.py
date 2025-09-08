import time
import json
from dotenv import load_dotenv
load_dotenv()

# File Importing
from utils.parse_conf import data_fetcher
from utils.parse_conf import datetime_converter
from conf import settings
from utils.parse_conf import major_order_parser
from utils.parse_conf import galaxy_stats_parser

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
user_timezone = "America/Toronto"

# Save JSON info to file function
def save_json_to_file(data, filename):
    try:
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4) 
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")


def main_program():
    """
        Main function for fetching and parsing data
    """
    print("\n---- Beginning new data refresh cycle ----")
    

    major_order_url = settings.urls.get("major_order")
    if major_order_url:
        major_orders_data = data_fetcher.fetch_data_from_url(major_order_url)
        if major_orders_data:
            # save_json_to_file(major_orders_data, "raw_mo_data") #<------- SAVES

            print("\nSuccessfully fetched raw data for Major Orders. Now parsing...")
            parsed_orders = major_order_parser.parse_major_order_data(major_orders_data, user_timezone)
            if parsed_orders:

                print("\nSuccesfully parsed the following Major Order(s):")
                for order in parsed_orders:
                    print(f"        {order.get("order_title")}") # "MAJOR ORDER or SECONDARY ORDER"
                    print("    -------------------")
                    
                    print(f"    Briefing: {order.get("order_briefing")}")
                    
                    tasks = order.get("tasks", [])
                    if tasks:
                        print("\n    --- OBJECTIVES ---")
                        for i, task in enumerate(tasks):
                            progress = task.get('progress', 0)
                            goal = task.get('goal', 1)
                            # Format with commas for readability
                            progress_str = f"{progress:,}"
                            goal_str = f"{goal:,}"
                            
                            print(f"    Objective {i+1}:")
                            print(f"        Task Type: {task.get('type')}")
                            print(f"        Target Planet ID: {task.get('target_planet_id')}")
                            print(f"        Progress: {progress_str} / {goal_str}")
                            # Simple percentage calculation
                            if goal > 0:
                                percentage = (progress / goal) * 100
                                print(f"        Completion: {percentage:.3f}%")
                        print("    ------------------")

                    print(f"    Order Expires: {order.get("order_expires")}")

                    if order.get("rewards"):
                        print(f"\n  Rewards: {order.get("rewards")} Medals")
                    else:
                        print("\n   This order type does not include any rewards.")
                        
            else:
                print("\nFailed to parse Major Orders data.")
        else:
            print("\nFailed to fetch Major Order data.")






    galaxy_stats_lib = settings.urls.get("planet_stats")
    galaxy_stats = galaxy_stats_lib


    if galaxy_stats:   
        galaxy_stats_data = data_fetcher.fetch_data_from_url(galaxy_stats)
        if galaxy_stats_data:
            print("\nSuccessfully fetched Galactic War statistics. Now parsing...")
            # Parse through for necessary key-pairs
            parsed_galaxy_stats = galaxy_stats_parser.parse_galaxy_stats(galaxy_stats_data)
            
            if parsed_galaxy_stats:
                print("\nSuccessfully parsed Galactic War stats:")

                # CONVERTS UTC INTO USER TIMEZONE (CANADA/EASTERN)
                print("\n---- GALACTIC WAR STATS ----")
                

                overall_stats = parsed_galaxy_stats.get("galaxy_stats", {})
                if overall_stats:
                    for key, value in overall_stats.items():
                        print(f"    {key.replace("_", " ").title()}: {value:,}")
                else:
                    print("No overall stats available.")

            else:
                print("\nFailed to parse Galactic War stats.")
        else:
            print("\nFailed to fetch Major Orders data from endpoint.")
    else:
        print("\nMajor Orders endpoint details not found in api_endpoints.py")

    print("\n---- Data refresh cycle complete ----")



if __name__ == "__main__":
    while True:
        main_program()
        print("\nWaiting 10 seconds before next refresh...")
        time.sleep(10)