# WAP to generate the Fibonacci series upto n.
def generate_fibonacci(n):
    """Generate Fibonacci series up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    
    return fibonacci_series

def main():
    try:
        n = int(input("Enter the number of terms: "))
        if n < 0:
            print("Please enter a positive integer.")
        else:
            fibonacci_series = generate_fibonacci(n)
            print(f"Fibonacci series up to {n} terms: {fibonacci_series}")
    
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
