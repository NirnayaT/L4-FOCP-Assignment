from typing import List, Tuple, Dict
from collections import defaultdict
from statistics import mean

def analyze_data(lap_times: List[Tuple[str, float]]) -> Dict:
    """
    Analyzes the lap time data with improved performance and type safety.

    Args:
        lap_times: List of (driver_code, lap_time) tuples
    Returns:
        Dictionary containing comprehensive analysis results
    """
    if not lap_times:
        return {
            "fastest_driver": None,
            "fastest_time": None,
            "driver_fastest": {},
            "driver_averages": {},
            "overall_average": None,
            "sorted_fastest_times": []
        }

    driver_times = defaultdict(list)

    # Group lap times by driver using list comprehension
    [driver_times[driver].append(time) for driver, time in lap_times]

    # Calculate metrics using dictionary comprehension
    driver_fastest = {
        driver: min(times) for driver, times in driver_times.items()
    }
    
    driver_averages = {
        driver: mean(times) for driver, times in driver_times.items()
    }

    # Find fastest driver using min() with key function
    fastest_driver, fastest_time = min(
        driver_fastest.items(),
        key=lambda x: x[1]
    )

    # Calculate overall average using flat list comprehension
    all_times = [time for times in driver_times.values() for time in times]
    overall_average = mean(all_times)

    # Sort fastest times
    sorted_fastest_times = sorted(
        driver_fastest.items(),
        key=lambda x: x[1],  
    )

    return {
        "fastest_driver": fastest_driver,
        "fastest_time": fastest_time,
        "driver_fastest": driver_fastest,
        "driver_averages": driver_averages,
        "overall_average": overall_average,
        "sorted_fastest_times": sorted_fastest_times
    }
