#5. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops)
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

input_list = input("Enter the elements of the list separated by spaces: ").split()
reversed_list = reverse_list(input_list)
print("Reversed list:", reversed_list)

