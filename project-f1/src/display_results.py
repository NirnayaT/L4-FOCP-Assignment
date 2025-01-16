import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
import json

def load_driver_details(file_name="data/drivers_info.json"):
    """
    Loads driver details from a JSON file.
    
    :param file_name: Path to the JSON file
    :return: Dictionary of driver details
    :raises: FileNotFoundError if file doesn't exist
    :raises: JSONDecodeError if JSON is invalid
    """
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON format: expected dictionary")
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Driver info file not found: {file_name}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in {file_name}: {str(e)}")


class TimingsBoardApp(tk.Tk):
    def __init__(self, grand_prix, analysis_results):
        super().__init__()
        
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.title("F1 Timing Board")
        self.geometry("1200x700")
        self.configure(bg='#15151E')
        
        self.grand_prix = grand_prix
        self.analysis_results = analysis_results
        self.driver_details = load_driver_details()
        
        self.apply_custom_styles()
        self.create_widgets()

    def apply_custom_styles(self):
        self.style.configure(
            "Custom.Treeview",
            background="#1E1E1E",
            foreground="#FFFFFF",
            fieldbackground="#1E1E1E",
            rowheight=45,
            font=("Arial", 11)
        )
        
        self.style.configure(
            "Custom.Treeview.Heading",
            background="#2A2A2A",
            foreground="#FFFFFF",
            font=("Arial", 12, "bold")
        )
        
        self.style.map("Custom.Treeview",
            background=[('selected', '#404040')],
            foreground=[('selected', '#FFFFFF')]
        )

    def create_widgets(self):
        # Header Frame
        header_frame = tk.Frame(self, bg='#15151E', height=100)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        # GP Title
        title_label = tk.Label(
            header_frame,
            text=f"{self.grand_prix}",
            font=("Arial", 28, "bold"),
            fg='#FFFFFF',
            bg='#15151E'
        )
        title_label.pack(pady=20)

        # Session Info Frame
        info_frame = tk.Frame(self, bg='#15151E')
        info_frame.pack(fill=tk.X, padx=20, pady=10)
        
        # Fastest Lap Info
        fastest_label = tk.Label(
            info_frame,
            text=f"Fastest Lap: {self.analysis_results['fastest_driver']} - {self.analysis_results['fastest_time']:.3f}s",
            font=("Arial", 14, "bold"),
            fg='#FFFFFF',
            bg='#15151E'
        )
        fastest_label.pack(side=tk.LEFT, padx=10)

        # Overall Average
        average_label = tk.Label(
            info_frame,
            text=f"Session Average: {self.analysis_results['overall_average']:.3f}s",
            font=("Arial", 14),
            fg='#FFFFFF',
            bg='#15151E'
        )
        average_label.pack(side=tk.RIGHT, padx=10)

        # Create Timing Table
        self.create_timing_table()

    def create_timing_table(self):
        table_frame = tk.Frame(self, bg='#15151E')
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        columns = ("Position", "Driver Code", "Driver Name", "Fastest Time", "Gap", "Average Time", "Team")
        table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Custom.Treeview"
        )

        column_widths = {
            "Position": 80,
            "Driver Code": 100,
            "Driver Name": 200,
            "Fastest Time": 120,
            "Gap": 100,
            "Average Time": 120,
            "Team": 180
        }

        for col, width in column_widths.items():
            table.heading(col, text=col)
            table.column(col, anchor="center", width=width)

        fastest_time = self.analysis_results['fastest_time']
        
        for pos, (driver_code, fastest_time_driver) in enumerate(self.analysis_results['sorted_fastest_times'], 1):
            driver_info = self.driver_details.get(driver_code, {})
            driver_name = driver_info.get('name', 'Unknown Driver')
            team = driver_info.get('team', 'Unknown Team')
            average_time = self.analysis_results['driver_averages'].get(driver_code, 0)
            gap = "-" if pos == 1 else f"+{fastest_time_driver - fastest_time:.3f}"
            
            tag = 'even' if pos % 2 == 0 else 'odd'
            table.insert("", "end", values=(
                f"P{pos}",
                driver_code,
                driver_name,
                f"{fastest_time_driver:.3f}",
                gap,
                f"{average_time:.3f}",
                team
            ), tags=(tag,))

        table.tag_configure('odd', background='#1E1E1E')
        table.tag_configure('even', background='#252525')

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)

        table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def display_results(grand_prix, analysis_results):
    """Initialize and run the Tkinter app to display results."""
    app = TimingsBoardApp(grand_prix, analysis_results)
    app.mainloop()
