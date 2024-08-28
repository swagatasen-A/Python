# Creating tuples
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'yogurt')

# I. Joining the tuples
food_stuff_tp = fruits + vegetables + animal_products

# II. Changing the tuple to a list
food_stuff_lt = list(food_stuff_tp)

# III. Slicing out the middle item(s)
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index-1:middle_index+1]
else:
    middle_items = [food_stuff_lt[middle_index]]

# IV. Slicing out the first and last three items
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# V. Deleting the tuple completely
del food_stuff_tp

print("Food stuff as list:", food_stuff_lt)
print("Middle item(s):", middle_items)
print("First three items:", first_three)
print("Last three items:", last_three)
