import json

filename = 'favorite_number.json'
try:
    with open(filename, 'r') as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    fav_num = input('What is your favorite number? ')
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
    
    print('We will store your favorite number here')
else:
    print(f'Your favorite number is {favorite_number}!')