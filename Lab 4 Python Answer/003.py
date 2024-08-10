# 3. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.Suppose the following input is supplied to the program:Hello worldPractice makes perfectThen, the output should be:HELLO WORLDPRACTICE MAKES PERFECT
def main():
    lines = []

    print("Enter lines of text (type 'END' to stop):")
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    for line in lines:
        print(line.upper())

if __name__ == "__main__":
    main()
