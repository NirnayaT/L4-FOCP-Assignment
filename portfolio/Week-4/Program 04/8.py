def process_flexible_temperatures():
    temps = []
    while True:
        temp_input = input("Enter temperature (or press Enter to finish): ")
        if temp_input == "":
            break
        value = float(temp_input[:-1])
        temps.append(value)
    
    if temps:
        print(f"Maximum: {max(temps)}C")
        print(f"Minimum: {min(temps)}C")
        print(f"Mean: {sum(temps)/len(temps):.1f}C")
    else:
        print("No temperatures entered")

process_flexible_temperatures()