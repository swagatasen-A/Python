# Get user input for two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Swap the numbers using a temporary variable
    temp = num1
    num1 = num2
    num2 = temp
    
    print(f"After swapping: \nFirst number: {num1}\nSecond number: {num2}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
