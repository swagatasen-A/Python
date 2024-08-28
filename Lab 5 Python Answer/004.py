# Creating sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Length of it_companies
length_it_companies = len(it_companies)

# II. Add 'Twitter'
it_companies.add('Twitter')

# III. Insert multiple IT companies
it_companies.update(['LinkedIn', 'Uber', 'Netflix'])

# IV. Remove a company
it_companies.remove('Oracle')  # Use discard if you're not sure if it exists

# V. Difference between remove and discard
# remove() throws an error if the item does not exist, while discard() does not.

print("IT companies:", it_companies)
print("Length of IT companies:", length_it_companies)

# Set operations with A and B
# I. Joining A and B
A_union_B = A.union(B)

# II. Intersection of A and B
A_intersection_B = A.intersection(B)

# III. Is A subset of B
A_subset_B = A.issubset(B)

# IV. Are A and B disjoint sets
A_disjoint_B = A.isdisjoint(B)

# V. Symmetric difference between A and B
A_symmetric_diff_B = A.symmetric_difference(B)

# VI. Delete the sets
del A, B

print("A union B:", A_union_B)
print("A intersection B:", A_intersection_B)
print("Is A subset of B:", A_subset_B)
print("Are A and B disjoint:", A_disjoint_B)
print("Symmetric difference:", A_symmetric_diff_B)
