# 8. Please write a program which count and print the numbers of each character in a string input by console.Example:If the following string is given as input to the program:abcdefgabc Then, the output of the program should be:a,2c,2b,2e,1d,1g,1f,1
def main():
    input_string = input("Enter a string: ")
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        print(f"{char},{count}")

if __name__ == "__main__":
    main()
