#4. Compute a)5 to the power of 8 b)square root of 400 c)exponent of 5 d)Logarithm of 625 base 5
import math

def compute_values():
    a = int(input("Enter the base number for power calculation: "))
    b = int(input(f"Enter the exponent to raise {a} to: "))
    
    c = int(input("Enter the number to compute the square root: "))
    
    d = int(input("Enter the number to compute the exponent (e^d): "))
    
    e = int(input("Enter the number to compute the logarithm: "))
    base = int(input(f"Enter the base for the logarithm of {e}: "))
    
    power_result = math.pow(a, b)
    sqrt_result = math.sqrt(c)
    exp_result = math.exp(d)
    log_result = math.log(e, base)
    
    print(f"{a} to the power of {b} is {power_result}")
    print(f"The square root of {c} is {sqrt_result}")
    print(f"The exponent of {d} (e^{d}) is {exp_result}")
    print(f"The logarithm of {e} base {base} is {log_result}")

compute_values()

