import json
from . import api_endpoints


def parse_major_order_data(data):
    
    parsed_orders = []
    
    if not isinstance(data, list):
        print(f"Error: Expected a list of major orders, but received {type(data)}")
        return None

    try:
        
        for order in data:
            mission_title = order.get("setting", {}).get("overrideTitle", order.get("title"))
            description = order.get("setting", {}).get("overrideBrief", order.get("briefing"))


            # Reward Parsing (to handle None exceptions)
            rewards = None

            reward_dict = order.get("reward")
            if isinstance(reward_dict, dict):
                rewards = reward_dict.get("amount")

            if rewards is None:
                rewards_list = order.get("rewards")
                if isinstance(rewards_list, list) and rewards_list and isinstance(rewards_list[0], dict):
                    rewards = rewards_list[0].get("amount")

            start_time = order.get("startTime")
            expiration_time = order.get("expiresIn")
            

            if mission_title and description:
                order_details = {
                    "missionType": mission_title,
                    "description": description,
                    "rewards": rewards,
                    "startTime": start_time,
                    "expirationTime": expiration_time
                }
                parsed_orders.append(order_details)
            else:
                print("Warning: Skipping an order due to missing title or description.")

        print(f"Successfully parsed {len(parsed_orders)} major orders.")
        return parsed_orders
            
    except (AttributeError, TypeError) as e:
        print ("Error processing major order's data: {e}")
        return None