#4. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.Suppose the following input is supplied to the program:hello world and practice makes perfect and hello world againThen, the output should be:again and hello makes perfect practice world
def main():
    input_string = input("Enter a sequence of whitespace-separated words: ")
    words = input_string.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    output_string = ' '.join(sorted_words)
    print(f"Sorted unique words: {output_string}")

if __name__ == "__main__":
    main()
