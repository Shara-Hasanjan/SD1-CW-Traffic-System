import tkinter as tk
import os
from process_data import load_traffic_data, process_csv_data, display_outcomes
from input_validation import validate_date_input
from text_file import save_results_to_txt_file

class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date
        self.root = tk.Tk()
        self.root.title("Histogram of Vehicle Frequency per Hour")
        self.canvas_width = 1000
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

    def setup_window(self):
        """
        Sets up the title and axis for the histogram.
        """
        self.canvas.create_text(
            self.canvas_width // 2, 30, 
            text=f"Histogram of Vehicle Frequency per Hour ({self.date})", 
            font=("Comic Sans MS", 16, "bold"),fill="#4E5054"
        )

        # Draw x-axis
        self.canvas.create_line(100, 550, 900, 550, fill="#88B7B6",width=1)  

        
        for hour in range(24):
            x = 100 + hour * 32
            self.canvas.create_text(x + 16, 570, text=f"{hour:02d}", font=("Comic Sans MS", 10),fill="#4E5054")

    def draw_histogram(self):
        """
        Draws the bars for the histogram and adds the accurate values on top of each bar.
        """
        max_value = max(
            max(self.traffic_data["Elm Avenue/Rabbit Road"]),
            max(self.traffic_data["Hanley Highway/Westway"])
        )
        scale = 350 / max_value  
        
        for hour in range(24):
            # Elm Avenue/Rabbit Road details
            elm_value = self.traffic_data["Elm Avenue/Rabbit Road"][hour]
            elm_height = elm_value * scale
            x1 = 100 + hour * 32
            y1 = 550 - elm_height
            x2 = x1 + 15
            self.canvas.create_rectangle(x1, y1, x2, 550, fill="#95FB92", outline="#88B7B6", width=1)  

           
            self.canvas.create_text(x1 + 15//2, y1 - 5, text=str(elm_value), font=("Arial", 8), fill="#72D07D")

            # Hanley Highway/Westway details
            hanley_value = self.traffic_data["Hanley Highway/Westway"][hour]
            hanley_height = hanley_value * scale
            x3 = x2 
            y3 = 550 - hanley_height
            x4 = x3 + 15
            self.canvas.create_rectangle(x3, y3, x4, 550, fill="#FC9493", outline="#88B7B6", width=1)  

           
            self.canvas.create_text(x3 + 15//2, y3 - 5, text=str(hanley_value), font=("Arial",8), fill="#CC7578")

    def add_legend(self):
        """
        Adds a legend to the histogram.
        """
        self.canvas.create_rectangle(750, 100, 770, 120, fill="#95FB92", outline="#88B7B6", width=1)  
        self.canvas.create_text(780, 110, text="Elm Avenue/Rabbit Road", anchor="w", font=("Comic Sans MS", 10,),fill="#4E5054")

        self.canvas.create_rectangle(750, 130, 770, 150, fill="#FC9493", outline="#88B7B6", width=1)  
        self.canvas.create_text(780, 140, text="Hanley Highway/Westway", anchor="w", font=("Comic Sans MS", 10),fill="#4E5054")

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        self.root.mainloop()


class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None

    def load_csv_file(self, file_path):
        """
        Loads a CSV file and processes its data.
        """
        try:
            
            output = process_csv_data(file_path)

           
            display_outcomes(output)
            save_results_to_txt_file(output)

           
            selected_date = file_path.split("traffic_data")[1].split(".")[0]  # Extract date from the file name
            selected_date_formatted = f"{selected_date[:2]}/{selected_date[2:4]}/{selected_date[4:]}"
            
            # Generate and display the histogram
            traffic_data = load_traffic_data(file_path, selected_date_formatted)
            if any(traffic_data["Elm Avenue/Rabbit Road"]) or any(traffic_data["Hanley Highway/Westway"]):
                app = HistogramApp(traffic_data, selected_date_formatted)
                app.run()
            else:
                print(f"No data available for {selected_date_formatted}.")

        except FileNotFoundError:
            print(f"File {file_path} not found in the 'data' folder. Please try again.")



    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        while True:
            user_input = input("Do you want to select a data file for a different date? (Y/N): ").strip().upper()
            if user_input == 'Y':
                return True 
            elif user_input == 'N':
                return False  
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        while True:
            
            csv_file = validate_date_input()

            
            self.load_csv_file(csv_file)

           
            self.clear_previous_data()

           
            if not self.handle_user_interaction():
                print("\nThank you for using the traffic data analysis program. Goodbye!")
                break  # Exit the loop if the user chooses not to continue


if __name__ == "__main__":
    processor = MultiCSVProcessor()
    processor.process_files()