import json

name = input('What is your name? ')
fav_num = input('What is your favorite number? ')

with open(f'{name.lower()}.json', 'w') as f:
    json.dump(fav_num, f)
