import requests
from . import api_endpoints
from . import major_order_parser


# API Data Endpoint Dictionaries
base_api_url = "https://api.helldivers2.dev"

# Fetch API data
def fetch_data_from_endpoint(endpoint_name):

    # Must identify with personal headers
    personal_headers = {
        "X-Super-Client": "Helldivers2StatusMonitorPersonalProject",
        "X-Super-Contact": "syyntacksgames@gmail.com"
    }
   
    endpoint_path = endpoint_name["path"]
    full_url = base_api_url + endpoint_path

    print(f"\nAttempting to fetch data from endpoint: {full_url}")

    try:
        response = requests.get(full_url, headers=personal_headers)
        response.raise_for_status() # Raises an exception if HTTP error encountered
        
        return response.json()
    except requests.exceptions.RequestException as exc:   # Define the exception as exc
        print(f"\nError fetching data from {endpoint_path} endpoint: {exc}") # Return the occurring exception
        return None