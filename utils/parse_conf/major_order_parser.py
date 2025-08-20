import datetime
import json
from . import api_endpoints
from . import datetime_converter



def parse_major_order_data(data, user_timezone="UTC"):
    
    parsed_orders = []
    
    if not isinstance(data, list):
        print(f"Error: Expected a list of major orders, but received {type(data)}")
        return None

    try:
        
        for order in data:
            setting = order.get("setting", {})
            # Parsing and defining raw data
            assignment_progress = order.get("progress")
            mission_title = setting.get("overrideTitle")
            briefing = setting.get("overrideBrief")
            description = setting.get("taskDescription")
            tasks = setting.get("tasks")

            expires_in_seconds = order.get("expiresIn")

            expiration_time = datetime_converter.expiration_time_format(expires_in_seconds, user_timezone) # Now takes into account user timezone.

            # Reward Parsing (to handle None exceptions)
            rewards = None
            
            reward_dict = setting.get("reward")
            if isinstance(reward_dict, dict):
                rewards = reward_dict.get("amount")

            if rewards is None:
                rewards_list = setting.get("rewards")
                if isinstance(rewards_list, list) and rewards_list and isinstance(rewards_list[0], dict):
                    rewards = rewards_list[0].get("amount")

            if mission_title:
                order_details = {
                    "missionType": mission_title,
                    "progress": assignment_progress,
                    "briefing": briefing,
                    "description": description,
                    "tasks": tasks,
                    "rewards": rewards,
                    "expirationTime": expiration_time
                }
                parsed_orders.append(order_details)
            else:
                print("Warning: Skipping an order due to missing title or description.")

        print(f"Successfully parsed {len(parsed_orders)} major orders.")
        return parsed_orders
            
    except (AttributeError, TypeError) as e:
        print (f"Error processing major order's data: {e}")
        return None