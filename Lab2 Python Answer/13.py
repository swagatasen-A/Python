#13. Write a Python program to print the first 6 terms of a geometric sequence starting with 2 and having a common ratio of 3.
def print_geometric_sequence(start, ratio, terms):
    
    current_term = start
    
    
    for i in range(terms):
        print(f"Term {i+1}: {current_term}")
        
        current_term *= ratio


start_term = 2
common_ratio = 3
number_of_terms = 6


print(f"Geometric sequence starting with {start_term} and common ratio {common_ratio}:")
print_geometric_sequence(start_term, common_ratio, number_of_terms)
