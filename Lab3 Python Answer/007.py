#7. Write a program to compute sin x for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving xn sin x = x - x3/3! + x5/5! - x7/7! + x9/9! .......
import math

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def compute_sin(x, n):
    sine_sum = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        sine_sum += term
    return sine_sum

# Example usage:
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter a positive integer n (number of terms): "))

sine_value = compute_sin(x, n)
print(f"The sine of {x} using {n} terms is: {sine_value}")
