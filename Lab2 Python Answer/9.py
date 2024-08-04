#9. Convert Decimal number to Binary
def decimal_to_binary(decimal_number):
    
    return bin(decimal_number)[2:]


try:
    decimal_number = int(input("Enter a decimal number: "))
    
   
    binary_number = decimal_to_binary(decimal_number)
    print(f"The binary representation of {decimal_number} is {binary_number}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
