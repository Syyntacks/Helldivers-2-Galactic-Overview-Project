import datetime
import json
from . import api_endpoints
from . import datetime_converter



def parse_major_order_data(data, user_timezone="UTC"):
    
    # List to hold multiple dictionaries
    parsed_orders = []
    
    if not isinstance(data, list):
        print(f"Error: Expected a list of major orders, but received {type(data)}")
        return None

    try:
        
        for order in data:
            order_details = {}

            order_details["order_id"] = order.get("id")
            order_details["order_expiration"] = datetime_converter.parse_iso_timestamp(order.get("expiration"), user_timezone)
            
            # Mission settings
            order_details["order_type"] = order.get("type")
            order_details["order_title"] = order.get("title")
            order_details["order_briefing"] = order.get("briefing")
            order_details["order_taskDescr"] = order.get("description")

            # Task-specifics
            tasks_list = order.get("tasks", [])
            progress_list = order.get("progress", [])
            parsed_tasks = [] # Holds parsed tasks

            for i, task in enumerate(tasks_list): # Enumerate turns a number into an index for a list
                task_details = {}
                values = task.get("values", [])
                valueTypes = task.get("valueTypes", [])
                value_map = dict(zip(valueTypes, values)) # Pair two value lists together

                task_details["type"] = task.get("type")
                task_details["goal"] = value_map.get(3) # 3 = goal
                task_details["target_planet_id"] = value_map.get(12) # 12 = Planet ID for MO

                if i < len(progress_list):
                    task_details["progress"] = progress_list[i]
                else:
                    task_details["progress"] = 0 # If no progress data available

                parsed_tasks.append(task_details)

            order_details["tasks"] = parsed_tasks

            # Reward Parsing
            reward_data = order.get("rewards")
            if reward_data and isinstance(reward_data, dict):
                order_details["rewards"] = reward_data.get("amount")
            else:
                order_details["rewards"] = None

            parsed_orders.append(order_details)

        print(f"Successfully parsed {len(parsed_orders)} major orders.")
        return parsed_orders
            
    except (AttributeError, TypeError) as e:
        print (f"Error processing major order's data: {e}")
        return None