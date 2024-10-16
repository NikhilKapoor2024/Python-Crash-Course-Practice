#8-3. T-Shirts
def make_shirt(size='large', msg='I love Python'):
    print(f"A {size} shirt that says '{msg}'.")

make_shirt('large', 'yo what up homie')
make_shirt(msg='ay yo yo what up dog', size='medium')
make_shirt()
make_shirt('medium', 'doobie doobie doo!')

#8-5. Cities
def describe_city(city, country="canada"):
    print(f"{city.title()} is in {country.title()}")

describe_city('toronto')
describe_city('quebec')
describe_city('chicago')