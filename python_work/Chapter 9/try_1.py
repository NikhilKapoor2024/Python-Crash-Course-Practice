# 9-1: Restaurant
class Restaurant:
    """class representation of a restaurant"""
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The {self.name} serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!\n")

restaurant = Restaurant("Nikhil's Neat Diner", 'bullshit')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants
chinese_restaurant = Restaurant('Golden Wok', 'chinese')
chinese_restaurant.describe_restaurant()
chinese_restaurant.open_restaurant()

mexican_restaurant = Restaurant('Mi Tierra Restaurante', 'mexican')
mexican_restaurant.describe_restaurant()
mexican_restaurant.open_restaurant()

italian_restaurant = Restaurant('Friggatoria Vomero', 'fried food')
italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()

# 9-3. Users
class User:
    """Class representation of a User"""

    def __init__(self, first_name, last_name, likes, dislikes):
        self.full_name = f"{first_name.title()} {last_name.title()}"
        self.likes = likes
        self.dislikes = dislikes
    
    def describe_user(self):
        print("User is:")
        print(f"- Name: {self.full_name}\n- Likes: {self.likes}\n- Dislikes: {self.dislikes}")
    
    def greet_user(self):
        print(f"Hello, {self.full_name}!")

user_tom = User('tom', 'king', 'comics', 'idk')
user_tom.greet_user()
user_tom.describe_user()
print("\n")

user_sarah = User('sarah', 'stash', 'drugs', 'not drugs')
user_sarah.greet_user()
user_sarah.describe_user()
print("\n")

user_bill = User('bill', 'burr', 'movies', 'racists')
user_bill.greet_user()
user_bill.describe_user()
print("\n")
