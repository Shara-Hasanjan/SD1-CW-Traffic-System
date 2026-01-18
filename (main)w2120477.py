# Author: A.T.H.I. Hasanjan
# Date: 10/12/2024
# Student ID: 20232856/w2120477

from input_validation import *
from process_data import *
from text_file import *
from histogram import *

def main():
    """
    Main function to run the program.
    Handles user input, processes data, and saves the results.
    """
    while True:
        # Get the file path based on user input
        csv_file = validate_date_input()
        try:
            # Process data from the file
            output = process_csv_data(csv_file)

            
            display_outcomes(output)
            save_results_to_txt_file(output)

            
            selected_date = csv_file.split("traffic_data")[1].split(".")[0]  
            selected_date_formatted = f"{selected_date[:2]}/{selected_date[2:4]}/{selected_date[4:]}"
            
            # Generate and display the histogram
            traffic_data = load_traffic_data(csv_file, selected_date_formatted)
            if any(traffic_data["Elm Avenue/Rabbit Road"]) or any(traffic_data["Hanley Highway/Westway"]):
                app = HistogramApp(traffic_data, selected_date_formatted)
                app.run()
            else:
                print(f"No data available for {selected_date_formatted}.")

        except FileNotFoundError:
            print(f"File {csv_file} not found in the 'data' folder. Please try again.")
            continue

        # Ask the user if they want to process another file
        while True:
            user_input = input("Do you want to select a data file for a different date? (Y/N): ").strip().upper()
            if user_input == 'Y':
                break  
            elif user_input == 'N':
                print("\nThank you for using the traffic data analysis program. Goodbye!")
                return 
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    main()

# if you have been contracted to do this assignment please do not remove this line