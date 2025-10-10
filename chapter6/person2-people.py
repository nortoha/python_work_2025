# Make an empty list to store people in.
people = []

# Define some people, and add them to the list.
person1 = {
    'first_name': 'johnny',
    'last_name': 'cash',
    'age': 71,
    'city': 'kingsland',
    }
people.append(person1)

person2 = {
    'first_name': 'willie',
    'last_name': 'nelson',
    'age': 92,
    'city': 'abbott',
    }
people.append(person2)

person3 = {
    'first_name': 'waylon',
    'last_name': 'jennings',
    'age': 65,
    'city': 'littlefield ',
    }
people.append(person3)

# Display all of the information in the dictionary.
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")
