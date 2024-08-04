#14. Print the series upto N terms: 1,2,6,24,120,720 
import math

def print_factorial_series(terms):
    for i in range(1, terms + 1):
        print(math.factorial(i), end=", " if i < terms else "\n")
try:
    n = int(input("Enter the number of terms to print in the series: "))
    
    if n < 1:
        print("Number of terms must be at least 1.")
    else:
        print(f"Factorial series up to {n} terms:")
        print_factorial_series(n)
        
except ValueError:
    print("Invalid input. Please enter a valid integer.")
