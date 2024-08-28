# Initial list of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# I. Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)

# II. Add the min age and the max age again to the list
ages.extend([min_age, max_age])

# III. Find the median age
n = len(ages)
median_age = (ages[n//2 - 1] + ages[n//2]) / 2 if n % 2 == 0 else ages[n//2]

# IV. Find the average age
average_age = sum(ages) / n

# V. Find the range of the ages
age_range = max_age - min_age

# VI. Compare the value of (min - average) and (max - average) using abs() method
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Age range:", age_range)
print("Difference between min and average:", min_diff)
print("Difference between max and average:", max_diff)
