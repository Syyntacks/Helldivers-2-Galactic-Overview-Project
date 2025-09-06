import time
import pytz
import json

# File Importing
from utils.parse_conf import data_fetcher
from utils.parse_conf import datetime_converter
from utils.parse_conf import api_endpoints
from utils.parse_conf import major_order_parser
from utils.parse_conf import war_details_parser

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
    

    major_order_endpoint = api_endpoints.api_endpoints.get("major_orders")
    if major_order_endpoint:
        major_orders_data = data_fetcher.fetch_data_from_endpoint(major_order_endpoint)
        if major_orders_data:
            # save_json_to_file(major_orders_data, "raw_mo_data") #<------- SAVES

            print("\nSuccessfully fetched raw data for Major Orders. Now parsing...")
            parsed_orders = major_order_parser.parse_major_order_data(major_orders_data, user_timezone)
            if parsed_orders:

                print("\nSuccesfully parsed the following Major Order(s):")
                for order in parsed_orders:
                    print("_____________________")
                    print(f"{order.get("order_title")}") # "MAJOR ORDER or SECONDARY ORDER"
                    print(f"Briefing: {order.get("order_briefing")}")
                    
                    # --- NEW DISPLAY LOOP FOR TASKS ---
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
                    # ------------------------------------
                    print(f"    Order Expires: {order.get("order_expiration")}")


                    if order.get("rewards"):
                        print(f"\n  Rewards: {order.get("rewards")} Medals")
                    else:
                        print("\n   This order type does not include any rewards.")
                        
            else:
                print("\nFailed to parse Major Orders data.")
        else:
            print("\nFailed to fetch Major Order data.")

    war_stats_endpoint = api_endpoints.api_endpoints.get("war_state")
    if war_stats_endpoint:   
        war_stats_data = data_fetcher.fetch_data_from_endpoint(war_stats_endpoint)
        if war_stats_data:
            print("\nSuccessfully fetched raw Galactic War stats. Now parsing...")
            # Parse through for necessary key-pairs
            parsed_war_stats = war_details_parser.parse_war_details(war_stats_data)
            
            if parsed_war_stats:
                print("\nSuccessfully parsed Galactic War stats:")

                # CONVERTS UTC INTO USER TIMEZONE (CANADA/EASTERN)
                start_time_utc = parsed_war_stats.get('start_time', "N/A")
                # end_time_utc = parsed_war_stats.get('end_time', "N/A")
                current_time_utc = parsed_war_stats.get('current_time', "N/A")
                print(f"    War started: {datetime_converter.parse_iso_timestamp(start_time_utc, user_timezone)}")
                # print(f"    War ends: {datetime_converter.parse_iso_timestamp(end_time_utc, user_timezone)}")
                print(f"    Current time: {datetime_converter.parse_iso_timestamp(current_time_utc, user_timezone)}")
                print(f"    Client version: {parsed_war_stats.get('client_version', "N/A")}")

                print("\n---- OVERALL WAR STATS ----")

                overall_stats = parsed_war_stats.get("overall_war_stats", {})
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