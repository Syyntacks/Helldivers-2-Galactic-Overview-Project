import time

# File Importing
from utils.parse_conf import data_fetcher
from utils.parse_conf import api_endpoints
from utils.parse_conf import major_order_parser
from utils.parse_conf import war_details_parser

def main_program():
    """
        Main function for fetching and parsing data
    """

    print("\n---- Beginning new data refresh cycle ----")
    major_order_endpoint = api_endpoints.api_endpoints.get("mo_overview")
    if major_order_endpoint:
        major_orders_data = data_fetcher.fetch_data_from_endpoint(major_order_endpoint)
        if major_orders_data:
            print("\nSuccessfully fetched raw data for Major Orders. Now parsing...")

            parsed_orders = major_order_parser.parse_major_order_data(major_orders_data)
            if parsed_orders:
                print("\nSuccesfully parsed the following Major Order(s):")
                for order in parsed_orders:
                    print("_____" * 2)
                    print(f"Mission type: {order.get('missionType')}")
                    print(f"Briefing: {order.get("briefing")}")
                    print(f"Description: {order.get('description')}")
                    # print(f"Tasks: {order.get("tasks")}")
                    print(f"Progress: {order.get("progress")}")
                    print(f"Rewards: {order.get("rewards")} Medals")
                    print(f"Expires: {order.get("expirationTime")}")
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

                # Top-level stats
                print(f"War ID: {parsed_war_stats.get('warId', "N/A")}")
                print(f"War started: {parsed_war_stats.get('start_time', "N/A")}")
                print(f"War ended: {parsed_war_stats.get('end_time', "N/A")}")
                print(f"Current time: {parsed_war_stats.get('current_time', "N/A")}")
                print(f"Client version: {parsed_war_stats.get('client_version', "N/A")}")

                print("\n---- OVERALL WAR STATS ----")

                overall_stats = parsed_war_stats.get("overall_war_stats", {})
                if overall_stats:
                    for key, value in overall_stats.items():
                        print(f"    {key.replace("_", " ").title()}: {value}")
                else:
                    print("   No overall stats available.")

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
        print("\nWaiting 12 seconds before next refresh...")
        time.sleep(12)