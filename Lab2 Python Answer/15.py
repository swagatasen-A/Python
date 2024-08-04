#15. Write a Python program that prompts the user to enter a base number and an exponentand then calculates the power of the base to the exponent. The program should not use the  exponentiation operator (**) or the math.pow() function.
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

try:
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    
    if exponent < 0:
        print("Exponent must be a non-negative integer.")
    else:
        result = power(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")
        
except ValueError:
    print("Invalid input. Please enter valid numerical values.")
