#  WAP to check whether a)is a perfect number b)is an Armstrong number
def is_perfect_number(num):
    """Check if a number is a perfect number."""
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def is_armstrong_number(num):
    """Check if a number is an Armstrong number."""
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)

def main():
    try:
        number = int(input("Enter a number: "))

        if is_perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")

        if is_armstrong_number(number):
            print(f"{number} is an Armstrong number.")
        else:
            print(f"{number} is not an Armstrong number.")
    
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
