#9. Print the pattern upto N Lines: 

def print_pattern(N):
    for n in range(1, N + 1):
        height = 2 * n - 1
        width = 2 * n + 1
        for i in range(1, height + 1):
            if i == 1:
                print(" " * (width // 2) + ".")
            elif i == height:
                print(" " * (width // 2 - i + 1) + "/" + "_" * (2 * (i - 1)) + "\\")
            else:
                print(" " * (width // 2 - i + 1) + "/" + " " * (2 * (i - 1)) + "\\")

# Example usage:
N = int(input("Enter the value of N: "))
print_pattern(N)

