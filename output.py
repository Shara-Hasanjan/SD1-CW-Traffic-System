
def format_output(key, value):
    """
    Formats the result based on the key and value.
    """
    if key == "file_name":
        return f"Data file selected is {value.split('/')[-1]}.\n"
    elif key == "total_vehicles":
        return f"The total number of vehicles recorded for this date is: {value}."
    elif key == "total_trucks":
        return f"The total number of trucks recorded for this date is: {value}."
    elif key == "total_electric":
        return f"The total number of electric vehicles for this date is: {value}."
    elif key == "two_wheeled":
        return f"The total number of two-wheeled vehicles for this date is: {value}."
    elif key == "headnorth_busses":
        return f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is: {value}."
    elif key == "no_turns":
        return f"The total number of Vehicles through both junctions not turning left or right is: {value}."
    elif key == "truck_percentage":
        return f"The percentage of total vehicles recorded that are trucks for this date is: {value}%."
    elif key == "average_bicycle":
        return f"The average number of Bikes per hour for this date is: {value}."
    elif key == "vehicles_over_speed_limit":
        return f"The total number of Vehicles recorded as over the speed limit for this date is: {value}."
    elif key == "elm_avenue_vehicles":
        return f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is: {value}."
    elif key == "hanley_highway_vehicles":
        return f"The total number of vehicles recorded through Hanley Highway/Westway junction is: {value}."
    elif key == "scooter_percentage":
        return f"{value}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters."
    elif key == "vehicles_in_busiest":
        return f"The highest number of vehicles in an hour on Hanley Highway/Westway is: {value}."
    elif key == "busiest_hour_times":
        return f"The most vehicles through Hanley Highway/Westway were recorded {', '.join(value)}."
    elif key == "rain_hours":
        return f"The number of hours of rain for this date is: {value} hrs."
    else:
        return f"{key}: {value}"
