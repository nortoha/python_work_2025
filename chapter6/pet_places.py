# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'goat',
    'name': 'cash',
    'owner': 'will',
    'weight': 70,
    'eats': 'grass',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'chicken',
    'owner': 'caroline',
    'weight': 2,
    'eats': 'grain',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'tanner',
    'owner': 'holly',
    'weight': 27,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

# Favorite places
favorite_places = {
    'kevin': ['bear mountain', 'death valley', 'tierra del fuego'],
    'holly': ['prince edward island', 'lake city colorado'],
    'reggie': ['mt. verstovia', 'iceland', 'new hampshire']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")
