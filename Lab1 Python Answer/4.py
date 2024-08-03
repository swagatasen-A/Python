# Function to reverse a number
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        # Extract the last digit
        last_digit = num % 10
        # Add the last digit to the reversed number
        reversed_num = reversed_num * 10 + last_digit
        # Remove the last digit from the original number
        num = num // 10
    return reversed_num

# Main function to execute the program
def main():
    # Get user input
    user_input = int(input("Enter a number to reverse: "))
    
    # Call the function to reverse the number
    reversed_num = reverse_number(user_input)
    
    # Display the reversed number
    print(f"The reverse of {user_input} is {reversed_num}")

# Entry point of the program
if __name__ == "__main__":
    main()
