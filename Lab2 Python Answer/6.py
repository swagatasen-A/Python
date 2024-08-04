#6. Define a sum function with two parameters and call the function
def sum_function(a, b):
    return a + b
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = sum_function(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

except ValueError:
    print("Invalid input. Please enter numerical values.")
