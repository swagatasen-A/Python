#3. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which  calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
import cmath

def _solve_quadratic_eqn(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Calculate two solutions using the quadratic formula
    sol1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    sol2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    return sol1, sol2

# Example usage with user input
try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    sol1, sol2 = _solve_quadratic_eqn(a, b, c)
    print(f"The solutions of the quadratic equation {a}x² + {b}x + {c} = 0 are {sol1} and {sol2}.")
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
