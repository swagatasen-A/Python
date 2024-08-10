#5. Write a program that accepts a sentence and calculate the number of letters and digits.Suppose the following input is supplied to the program:hello world! 123Then, the output should be:LETTERS 10DIGITS 3
def main():
    input_string = input("Enter a sentence: ")
    letter_count = 0
    digit_count = 0
    for char in input_string:
        if char.isalpha():  
            letter_count += 1
        elif char.isdigit():  
            digit_count += 1
    print(f"LETTERS {letter_count}")
    print(f"DIGITS {digit_count}")

if __name__ == "__main__":
    main()
