#11. Write a program in Python to find the sum of digits of a number.
def sum_of_digits(number):
    
    digits = str(abs(number))  
    total = sum(int(digit) for digit in digits)
    
    return total


try:
    num = int(input("Enter a number to find the sum of its digits: "))
    
    
    result = sum_of_digits(num)
    print(f"The sum of the digits of {num} is {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
