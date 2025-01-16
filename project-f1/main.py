import sys
from src.file_processor import process_file
from src.data_analysis import analyze_data
from src.display_results import display_results

def main():
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_name>")
        return

    file_name = sys.argv[1]

    try:
        # Process the input file
        grand_prix, lap_times = process_file(file_name)

        # Analyze the data
        analysis_results = analyze_data(lap_times)

        # Display the results in the GUI
        display_results(grand_prix, analysis_results)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
