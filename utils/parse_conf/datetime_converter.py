import datetime
import pytz

def expiration_time_format(seconds_remaining, timezone_str="UTC"):

    if seconds_remaining is None or not isinstance(seconds_remaining, int):
        return "N/A"
    
    try:
        # Get current UTC time
        now_utc = datetime.datetime.now(datetime.timezone.utc)

        # Add the remaining seconds to the current time to calculate expiration date
        expiration_datetime_utc = now_utc + datetime.timedelta(seconds=seconds_remaining)


        # 08-19-25: adding in timezone converter using pytz package.
        if timezone_str == "UTC":
            local_dt = expiration_datetime_utc
        else:
            try:
                local_timezone = pytz.timezone(timezone_str) # Figure out timezone str.
                local_dt = expiration_datetime_utc.astimezone(local_timezone) # Changes to new timezone.
            except pytz.UnknownTimeZoneError:
                print(f"Warning: Received unknown timezone '{timezone_str}'. Displaying in UTC instead.")
                local_dt = expiration_datetime_utc

        return local_dt.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    except (ValueError, TypeError) as e:
        return f"Invalid time value: {e}"




def parse_iso_timestamp(iso_string, timezone_str="UTC"):

    if iso_string is None:
        return None
    
    try:
        dt_object_utc = datetime.datetime.fromisoformat(iso_string.replace('Z', "+00:00"))

        # 08-19-25: adding in timezone converter using pytz package.
        if timezone_str == "UTC":
            local_dt = dt_object_utc
        else:
            try:
                local_timezone = pytz.timezone(timezone_str) # Figure out timezone str.
                local_dt = dt_object_utc.astimezone(local_timezone) # Changes to new timezone.
            except pytz.UnknownTimeZoneError:
                print(f"Warning: Received unknown timezone '{timezone_str}'. Displaying in UTC instead.")
                local_dt = dt_object_utc


        return local_dt.strftime("%Y-%m-%d %H:%M:%S %Z%z")
    except (ValueError, TypeError):
        return "\nInvalid Timestamp format"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    

# Assists with Major Order datetime.
def parse_numeric_timestamp(numeric_timestamp, timezone_str="UTC"):
    if not isinstance(numeric_timestamp, (int, float)):
        return "N/A"
    
    try:
        dt_object_utc = datetime.datetime.fromtimestamp(numeric_timestamp, datetime.timezone.utc)

        # Local time conversion
        if timezone_str == "UTC":
            local_dt = dt_object_utc
        else:
            try:
                local_timezone = pytz.timezone(timezone_str)
                local_dt = dt_object_utc.astimezone(local_timezone)
            except pytz.UnknownTimeZoneError:
                print(f"Warning: Received unknown timezone '{timezone_str}'. Displaying in UTC instead.")
                local_dt = dt_object_utc

        return local_dt.strftime("%Y-%m-%d %H:%M:$S %Z%z")
    except (ValueError, TypeError) as e:
        return f"Invalid numeric timestamp value: {e}"