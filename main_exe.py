import time
import requests
import json
import os

# File Importing
from utils.parse_conf import data_fetcher
from utils.parse_conf import api_endpoints
from utils.parse_conf import major_order_parser

def main_program():
    """
        Main function for fetching and parsing data
    """

    print("\n---- Beginning new data refresh cycle ----")
    mo_overview_details = api_endpoints.api_endpoints.get("mo_overview")
    if mo_overview_details:
        major_orders_data = data_fetcher.fetch_data_from_endpoint(mo_overview_details)
        if major_orders_data:
            print("\nSuccessfully fetched raw data for Major Orders. Now parsing...")

            parsed_orders = major_order_parser.parse_major_order_data(major_orders_data)
            if parsed_orders:
                print("\nSuccesfully parsed the following Major Orders:")
                for order in parsed_orders:
                    print("_____" * 2)
                    print(f"Mission type: {order.get('missionType')}")
                    print(f"Description: {order.get('description')}")
                    print(f"Rewards: {order.get("rewards")} Medals")
            else:
                print("\nFailed to parse Major Orders data.")
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