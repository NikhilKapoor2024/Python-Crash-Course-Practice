#6-7 People
person_a = {
    'f_name': 'Yash',
    'l_name': 'Kapoor',
    'age': 23,
    'city': 'San Antonio',
}
person_b = {
    'f_name': 'george',
    'l_name': 'costanza',
    'age': 34,
    'city': 'new york city'
}
person_c = {
    'f_name': 'stacy',
    'l_name': 'fakename',
    'age': 'nebulous',
    'city': 'mentopolis'
}

persons = [person_a, person_b, person_c]
for person in persons:
    print("Here's everything we know about this person:")
    full_name = f"{person['f_name']} {person['l_name']}"
    print(f"\tName: {full_name.title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tLocation: {person['city'].title()}")
print("\n")

#6-8 Pets
pet_a = {
    'name': 'zoe',
    'type': 'dog (blue healer)',
    'owner': 'nikhil'
}
pet_b = {
    'name': 'hope',
    'type': 'cat (russian blue)',
    'owner': 'nikolina'
}
pet_c = {
    'name': 'castillo',
    'type': 'parrot (african grey)',
    'owner': 'larry'
}
pets = [pet_a, pet_b, pet_c]
for pet in pets:
    print("Here's everything about this pet:")
    print(f"\tName: {pet['name'].title()}")
    print(f"\tType: {pet['type'].title()}")
    print(f"\tOwner: {pet['owner'].title()}")
print("Pets are adorable!")
print("\n")

#6-9 Favorite Places
favorite_places = {
    'nikhil': ['spain', 'england', 'italy'],
    'billy': ['new mexico', 'san fransisco', 'seattle'],
    'sasha': ['japan', 'india', 'portugal']
}
for person in favorite_places.keys():
    print(f"{person.title()}'s favorite places are:")
    for place in favorite_places[person]:
        print(f"\t{place.title()}")
print("\n")

#6-10 Favorite Places
favorite_numbers = {
    'nikhil': [23, 17, 100],
    'billy': [10, 20, 30],
    'sasha': [1, 2, 3]
}
for person in sorted(favorite_numbers.keys()):
    print(f"{person.title()}'s favorite numbers are:")
    for numbers in favorite_numbers[person]:
        print(f"\t{numbers}")
print("\n")

#6-11 Cities
cities = {
    'new york city': {
        'country': 'new york',
        'population': '8.336 million',
        'fact': 'It probably is the most notable thing about it.'
    },
    'chicago': {
        'country': 'illinois',
        'population': '2.665 million',
        'fact': 'The show "The Bear" features this city prominently.'
    },
    'los angeles': {
        'country': 'california',
        'population': '3.822 million',
        'fact': 'This is where Hollywood is.'
    }
}
for city, city_info in cities.items():
    print(f"Here's information about {city.title()}:")
    print(f"\tCountry: {city_info['country'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")
print("\n")