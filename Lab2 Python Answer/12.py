#12. Write a program in Python that prompts the user to input a number and prints its  multiplication table.
def print_multiplication_table(number, up_to=10):
    
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")
try:
    num = int(input("Enter a number to print its multiplication table: "))
    
    print(f"Multiplication table for {num}:")
    print_multiplication_table(num)
    
except ValueError:
    print("Invalid input. Please enter a valid integer.")
