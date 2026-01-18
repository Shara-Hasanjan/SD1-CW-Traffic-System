import csv
from output import *

def process_csv_data(file_path):
    """
    Reads the CSV file and calculates traffic data statistics.
    """
    output = {
        "file_name": file_path,
        "total_vehicles": 0,
        "total_trucks": 0,
        "total_electric": 0,
        "two_wheeled": 0,
        "headnorth_busses": 0,
        "no_turns": 0,
        "truck_percentage":0,
        "average_bicycle":0,
        "vehicles_over_speed_limit": 0,
        "elm_avenue_vehicles": 0,
        "hanley_highway_vehicles": 0,
        "scooter_percentage": 0,
        "vehicles_in_busiest":0,
        "busiest_hour_times": [],
        "rain_hours": 0,
    }

    traffic = {}
    rain_hours_set = set()
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
    

        for row in reader:
            output["total_vehicles"] += 1
            if row["VehicleType"]== "Truck":
                output["total_trucks"] += 1
            if row["elctricHybrid"].lower() == "true":
                output["total_electric"] += 1
            if row["VehicleType"] in ["Bicycle", "Motorcycle", "Scooter"]:
                output["two_wheeled"] += 1
            if row["JunctionName"] == "Elm Avenue/Rabbit Road" and row["travel_Direction_out"] == "N" and row["VehicleType"] == "Buss":
                output["headnorth_busses"] += 1
            if row["travel_Direction_in"] == row["travel_Direction_out"]:
                output["no_turns"] += 1
            output["truck_percentage"]
            if row["VehicleType"] == "Bicycle":
                output["average_bicycle"] += 1
            if int(row["VehicleSpeed"]) > int(row["JunctionSpeedLimit"]):
                output["vehicles_over_speed_limit"] += 1
            if row["JunctionName"] == "Elm Avenue/Rabbit Road":
                output["elm_avenue_vehicles"] += 1
            if row["JunctionName"] == "Hanley Highway/Westway":
                output["hanley_highway_vehicles"] += 1
                hour = row["timeOfDay"].split(":")[0]  
                if hour in traffic:
                    traffic[hour] += 1
                else:
                    traffic[hour] = 1
            if row["VehicleType"] == "Scooter" and row["JunctionName"] == "Elm Avenue/Rabbit Road":
                output["scooter_percentage"] += 1

            output["vehicles_in_busiest"]
            if row["Weather_Conditions"] in ["Rain","Light Rain","Heavy Rain"]:
                hour = row["timeOfDay"].split(":")[0]  
                rain_hours_set.add(hour)

        # Calculate percentages and averages  
        output["scooter_percentage"] = round((output["scooter_percentage"] / output["elm_avenue_vehicles"]) * 100) 
        output["truck_percentage"] = round((output["total_trucks"] / output["total_vehicles"]) * 100) 
        output["average_bicycle"] = round(output["average_bicycle"] / 24)
        output["rain_hours"] = len(rain_hours_set)

        if traffic:
            max_traffic = max(traffic.values())
            output["vehicles_in_busiest"] = max_traffic
            output["busiest_hour_times"] = [
                f"Between {hour}:00 and {int(hour) + 1:02}:00"
                for hour, count in traffic.items() if count == max_traffic
            ]
        
        

    return output

def load_traffic_data(file_path, selected_date):
    """
    Extracts hourly traffic data for a specific date.
    """
    traffic_data = {
        "Elm Avenue/Rabbit Road": [0] * 24,
        "Hanley Highway/Westway": [0] * 24,
    }

    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] == selected_date:
                hour = int(row["timeOfDay"].split(":")[0])  # Extract hour from time (HH:MM)
                if row["JunctionName"] == "Elm Avenue/Rabbit Road":
                    traffic_data["Elm Avenue/Rabbit Road"][hour] += 1
                elif row["JunctionName"] == "Hanley Highway/Westway":
                    traffic_data["Hanley Highway/Westway"][hour] += 1

    return traffic_data

def display_outcomes(output):
    """
    Prints all results to the console.
    """
    for key, value in output.items():
        print(format_output(key, value))
