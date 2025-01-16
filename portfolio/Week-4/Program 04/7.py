def process_temperatures():
    temps = []
    for i in range(6):
        temp_input = input(f"Enter temperature {i+1} (e.g., 23C): ")
        value = float(temp_input[:-1])
        temps.append(value)
    
    print(f"Maximum: {max(temps)}C")
    print(f"Minimum: {min(temps)}C")
    print(f"Mean: {sum(temps)/len(temps):.1f}C")

process_temperatures()