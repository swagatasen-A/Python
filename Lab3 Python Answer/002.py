#2. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    # Check if x1 and x2 are the same to avoid division by zero
    if x1 == x2:
        return "Slope is undefined (vertical line)."
    
    # Calculate the slope
    slope = (y2 - y1) / (x2 - x1)
    return slope

# Example usage with user input
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    slope = calculate_slope(x1, y1, x2, y2)
    print(f"The slope of the line through points ({x1}, {y1}) and ({x2}, {y2}) is {slope}.")
except ValueError:
    print("Please enter valid numbers.")
