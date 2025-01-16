import sys
import statistics

if len(sys.argv) > 1:
    temps = [float(x) for x in sys.argv[1:]]
    print(f"Maximum: {max(temps)}")
    print(f"Minimum: {min(temps)}")
    print(f"Mean: {statistics.mean(temps)}")
else:
    print("Please provide temperature values")
