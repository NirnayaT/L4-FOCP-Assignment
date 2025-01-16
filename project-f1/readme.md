# F1 Timing Board Project

## Overview
This program analyzes Formula 1 practice session lap timing data and presents comprehensive performance metrics through an intuitive graphical interface.

## Features
- Displays the Grand Prix name and session details
- Identifies the fastest driver and their lap time
- Displays the fastest lap time and average time for each driver
- Ranks drivers by their fastest lap times in descending order
- Displays results in a user-friendly GUI using Tkinter
- Supports additional driver details (name, team) via JSON

## Project Structure
- `main.py`: Entry point of the application
- `src/file_processor.py`: Handles input file reading and data extraction
- `src/data_analysis.py`: Processes lap times and calculates statistics
- `src/display_results.py`: Manages the GUI display using Tkinter

## Installation
1. Clone the repository
```bash
git clone https://github.com/NirnayaT/project-f1.git
```
2. Create a virtual environment
```bash
python -m venv venv
```
3. Activate the virtual environment
```bash
venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run the application:
```bash
python main.py <timing_data_file>
```

## Input File Format
The program expects a text file containing:
- First line: Grand Prix name
- Subsequent lines: Driver lap times in the format `DriverIDLapTime` (no separator)

Example:

```bash
Silverstone Grand Prix 
HAM90.123 
VER88.456 
LEC91.789 
ALO92.345 
```
## Dependencies
- Python 3.12.5 or below
- Tkinter for GUI implementation
- Additional requirements listed in requirements.txt