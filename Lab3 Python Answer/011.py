# 11. Print the pattern upto N lines:

def print_pattern(N):
    current_number = 1
    
    for n in range(1, N + 1):
        if n % 2 == 1:  
            for i in range(n):
                print(current_number, end=" ")
                current_number += 1
            print()
        else:  
            temp = current_number + n - 1
            for i in range(n):
                print(temp, end=" ")
                temp -= 1
            current_number += n
            print()

N = int(input("Enter the value of N: "))
print_pattern(N)
