import json

try:
    with open('nikhil.json', 'r') as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    print(contents)