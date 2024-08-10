# 2.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.Suppose the following input is supplied to the program:without,hello,bag,worldThen, the output should be:bag,hello,without,world
def main():
    input_string = input("Enter a comma-separated sequence of words: ")
    words = [word.strip() for word in input_string.split(',')]
    words.sort()
    sorted_string = ','.join(words)
    print(f"Sorted sequence: {sorted_string}")

if __name__ == "__main__":
    main()
