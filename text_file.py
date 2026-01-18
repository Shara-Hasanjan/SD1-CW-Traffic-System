from output import *

def save_results_to_txt_file(output, file_name="results.txt"):
    """
    Saves results to a text file.
    """
    with open(file_name, mode="a") as file:
        file.write("------------------ Results --------------------\n")
        for key, value in output.items():
            formatted_line = format_output(key, value) + "\n" 
            file.write(formatted_line)
        file.write("\n")