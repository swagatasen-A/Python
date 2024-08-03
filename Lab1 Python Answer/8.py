# WAP to check whether a number is a palindrome or not
def is_palindrome(number):
    # Convert the number to string
    str_num = str(number)
    
    # Reverse the string and compare with the original string
    if str_num == str_num[::-1]:
        return True
    else:
        return False

# Get user input
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
