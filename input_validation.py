import os

def validate_date_input():
    """
    Gets date input from the user and creates a file path.
    Ensures input is valid.
    """
    while True:
        try:
            day = int(input("Please enter the day of the survey in the format DD: "))
            if not (1 <= day <= 31):
                raise ValueError("Out of range - value must be in the range 1 to 31.")
            
            month = int(input("Please enter the month of the survey in the format MM: "))
            if not (1 <= month <= 12):
                raise ValueError("Out of range - value must be in the range 1 to 12.")
            
            year = int(input("Please enter the year of the survey in the format YYYY: "))
            print()
            if not (2000 <= year <= 2024):
                raise ValueError("Out of range - value must lie in the range 2000 to 2024.")
            
            file_name = f"traffic_data{day:02}{month:02}{year}.csv"
            file_path = os.path.join("data", file_name)
            return file_path
        except ValueError as e:
            print(e)
        