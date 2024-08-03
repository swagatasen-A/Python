def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
