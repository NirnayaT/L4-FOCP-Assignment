def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def test_conversions():
    celsius = 100
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
    print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C")

test_conversions()