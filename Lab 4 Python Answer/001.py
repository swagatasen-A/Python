# 1. Write a program to enter a string. Calculate the length of the string. Find the substring country. Count the occurences of each word in the given sentence.If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.
def main():
    input_string = input("Enter a string: ")
    string_length = len(input_string)
    print(f"Length of the string: {string_length}")
    substring = "country"
    if substring in input_string:
        print(f'The substring "{substring}" is found in the string.')
    else:
        print(f'The substring "{substring}" is not found in the string.')
    words = input_string.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("\nWord occurrences in the string:")
    for word, count in word_count.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    main()
