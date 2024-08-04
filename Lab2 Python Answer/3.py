#3. Find GCD of two numbers
import math
def find_gcd(num1, num2):
    return math.gcd(num1, num2)
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd_result = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd_result}")
