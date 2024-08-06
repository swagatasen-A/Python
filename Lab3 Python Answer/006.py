#6. Compute the sum up to n terms in the series 1 - 1/2 + 1/3 - 1/4 + 1/5 -... 1/n where n is a positive integer and input by user.
def compute_series_sum(n):
    total_sum = 0.0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total_sum -= 1 / i
        else:
            total_sum += 1 / i
    return total_sum

n = int(input("Enter a positive integer n: "))
series_sum = compute_series_sum(n)
print(f"The sum of the series up to {n} terms is: {series_sum}")
