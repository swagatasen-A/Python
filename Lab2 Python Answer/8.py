#8. Write a function to calculate the power of a number using recursion
def power(base, exponent):
    
    if exponent == 0:
        return 1
    
    else:
        return base * power(base, exponent - 1)

try:
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent (non-negative integer): "))
    
    if exponent < 0:
        print("Exponent should be a non-negative integer.")
    else:
        
        result = power(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")

except ValueError:
    print("Invalid input. Please enter numerical values.")
