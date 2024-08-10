#9.Write a program that accepts a string I. 1.reverses it. II. 2.checks whether it is a palindrome.III. 3.checks whether it ends with a specific substring.IV. 4.capitalize the first letter of each word in a stringV. 5.check if a string is anagram of another stringVI. 6.remove vowels from stringVII. 7.find length of the longest word in a sentence
def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == reverse_string(s)

def ends_with(s, substring):
    return s.endswith(substring)

def capitalize_first_letter(s):
    return ' '.join(word.capitalize() for word in s.split())

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def length_of_longest_word(s):
    words = s.split()
    return max(len(word) for word in words)

def main():
    input_string = input("Enter a string: ")
    print("Reversed String:", reverse_string(input_string))
    if is_palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    substring = input("Enter a substring to check: ")
    if ends_with(input_string, substring):
        print(f"The string ends with '{substring}'.")
    else:
        print(f"The string does not end with '{substring}'.")
    print("Capitalized String:", capitalize_first_letter(input_string))
    second_string = input("Enter another string to check if it's an anagram: ")
    if is_anagram(input_string, second_string):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
    print("String without vowels:", remove_vowels(input_string))
    print("Length of the longest word:", length_of_longest_word(input_string))

if __name__ == "__main__":
    main()
