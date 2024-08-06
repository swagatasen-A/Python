#10. Print a number as a 8 segment display N Lines: 
def print_digit(digit):
    segments = {
        '0': [" _ ",
              "| |",
              "|_|"],
        '1': ["   ",
              "  |",
              "  |"],
        '2': [" _ ",
              " _|",
              "|_ "],
        '3': [" _ ",
              " _|",
              " _|"],
        '4': ["   ",
              "|_|",
              "  |"],
        '5': [" _ ",
              "|_ ",
              " _|"],
        '6': [" _ ",
              "|_ ",
              "|_|"],
        '7': [" _ ",
              "  |",
              "  |"],
        '8': [" _ ",
              "|_|",
              "|_|"],
        '9': [" _ ",
              "|_|",
              " _|"]
    }
    return segments[digit]

def print_8_segment_display(N):
    for n in range(N):
        number = input(f"Enter a number for line {n+1}: ")
        for i in range(3):  
            line = ""
            for digit in number:
                line += print_digit(digit)[i] + " "
            print(line)


N = int(input("Enter the number of lines (N): "))
print_8_segment_display(N)
