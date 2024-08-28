# Creating the person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# I. Check if 'skills' key exists and print the middle skill
if 'skills' in person:
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    print("Middle skill:", middle_skill)

# II. Check if 'skills' key exists and if 'Python' is a skill
if 'skills' in person and 'Python' in person['skills']:
    print("Person has Python skill:", True)

# III. Determine the person's title
if set(['JavaScript', 'React']) == set(person['skills']):
    print('He is a front end developer')
elif set(['Node', 'Python', 'MongoDB']).issubset(set(person['skills'])):
    print('He is a backend developer')
elif set(['React', 'Node', 'MongoDB']).issubset(set(person['skills'])):
    print('He is a fullstack developer')
else:
    print('unknown title')

# IV. Check if married and lives in Finland
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
