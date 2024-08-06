#12. Write a python script that displays the following table
def display_table(rows):
    for i in range(1, rows + 1):
        row = [i]  
        for j in range(5):
            row.append(i ** j)  
        print(" ".join(map(str, row)))

rows = 5
display_table(rows)
