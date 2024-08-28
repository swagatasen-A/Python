# Creating the student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 21,
    'marital_status': 'Single',
    'skills': ['Python', 'C++'],
    'country': 'USA',
    'city': 'New York',
    'address': '1234 Main St'
}

# I. Length of the student dictionary
length_student_dict = len(student)

# II. Get value of skills and check the data type
skills = student.get('skills')
skills_type = type(skills)

# III. Modify the skills
student['skills'].extend(['Java', 'JavaScript'])

# IV. Get dictionary keys as a list
keys_list = list(student.keys())

# V. Get dictionary values as a list
values_list = list(student.values())

# VI. Change the dictionary to a list of tuples
student_items = list(student.items())

# VII. Delete one item
del student['address']

# VIII. Delete the dictionary completely
del student

print("Student dictionary length:", length_student_dict)
print("Skills:", skills)
print("Skills data type:", skills_type)
print("Student dictionary keys:", keys_list)
print("Student dictionary values:", values_list)
print("Student dictionary as list of tuples:", student_items)
