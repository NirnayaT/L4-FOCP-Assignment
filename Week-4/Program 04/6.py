def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temp():
    temp_input = input("Enter temperature (e.g., 23C): ")
    value = float(temp_input[:-1])
    result = celsius_to_fahrenheit(value)
    print(f"{result:.1f}F")
    
convert_temp()
