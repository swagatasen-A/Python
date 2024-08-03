# Function to find and display numbers between 1000 and 2000 that are divisible by 7 but not multiples of 5
def find_numbers():
    result = []
    for number in range(1000, 2001):
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    return result

# Main code
if __name__ == "__main__":
    # Get the numbers that match the criteria
    numbers = find_numbers()
    
    # Display the numbers
    print("Numbers between 1000 and 2000 that are divisible by 7 but not multiples of 5 are:")
    print(numbers)
