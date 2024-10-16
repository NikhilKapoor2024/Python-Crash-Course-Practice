#6-1 Person
person = {
    'f_name': 'Yash',
    'l_name': 'Kapoor',
    'age': 23,
    'city': 'San Antonio',
}
print(person)

#6-2 Favorite Numbers
fav_nums = {
    'james': 24,
    'sarah': 56,
    'george': 45,
    'tracy': 90,
    'leland': 12
}
print(f"James: {fav_nums['james']}")
print(f"Sarah: {fav_nums['sarah']}")
print(f"George: {fav_nums['sarah']}")
print(f"George: {fav_nums['george']}")
print(f"Tracy: {fav_nums['tracy']}")
print(f"Leland: {fav_nums['leland']}")

#6-3 Glossary
glossary = {
    'pencil': 'a tool used for writing on paper',
    'eraser': 'a tool for rubbing out writings',
    'book': 'a collection of papers for reading',
    'stepladder': 'a small ladder',
    'ladder': 'a long stepladder'
}
print(f"\nPencil: {glossary['pencil']}")
print(f'\nEraser: {glossary['eraser']}')
print(f"\nBook: {glossary['book']}")
print(f"\nStepladder: {glossary['stepladder']}")
print(f"\nLadder: {glossary['ladder']}")

#6-4 Glossary 2
for word, defn in glossary.items():
    print(f"\n{word.title()}: {defn}")

#6-5 Rivers
rivers = {
    'nile': 'egypt',
    'hudson': 'new york',
    'saar': 'germany'
}
print("\nRivers and Country:")
for r, c in rivers.items():
    print(f"The {r.title()} runs through {c.title()}")

print("\nRivers:")
for river in sorted(rivers.keys()):
    print(river.title())

print("\nCountries:")
for country in sorted(rivers.values()):
    print(country.title())

#6-6 Polling
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
potential_names = ['jen','edward', 'steve', 'jerry', 'phil']
dict_names = favorite_languages.keys()
for name in potential_names:
    if name not in dict_names:
        print(f"{name.title()}, please enter the poll!")
    else:
        print(f"Thank you for participating in the poll, {name.title()}.")