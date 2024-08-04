#10. Write a program in Python to check if a number is Krishnamurthy number.
import math

def is_krishnamurthy_number(number):
    
    digits = str(number)
    
    
    sum_of_factorials = sum(math.factorial(int(digit)) for digit in digits)
    
    
    return sum_of_factorials == number


try:
    num = int(input("Enter a number to check if it is a Krishnamurthy number: "))
    
    if is_krishnamurthy_number(num):
        print(f"{num} is a Krishnamurthy number.")
    else:
        print(f"{num} is not a Krishnamurthy number.")
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")
