# 9-4: Number Served
class Restaurant:
    """class representation of a restaurant"""
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The {self.name} serves {self.cuisine_type}. It has served {self.number_served} people.")

    def set_number_served(self, served):
        self.number_served = served

    def increment_num_served(self, add_served):
        if add_served >= 1:
            self.number_served += add_served
        else:
            print("You can't serve a negative amount of people!")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!\n")

restaurant = Restaurant('Hopdaddy', 'BBQ')
restaurant.describe_restaurant()
restaurant.set_number_served(20)
restaurant.describe_restaurant()
restaurant.increment_num_served(-3)
restaurant.describe_restaurant()
restaurant.increment_num_served(4)
restaurant.describe_restaurant()

# 9-5: Login Attempts
class User:
    """Class representation of a User"""
    def __init__(self, first_name, last_name, likes, dislikes):
        self.full_name = f"{first_name.title()} {last_name.title()}"
        self.likes = likes
        self.dislikes = dislikes
        self.login_attempts = 0
    
    def describe_user(self):
        print("User is:")
        print(f"- Name: {self.full_name}\n- Likes: {self.likes}\n- Dislikes: {self.dislikes}")
    
    def greet_user(self):
        print(f"Hello, {self.full_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"User {self.full_name} has attempted {self.login_attempts} logins.")
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"User {self.full_name} has reset their login attempts to zero.")
    
nik_kap = User('Nikhil', 'Kapoor', 'Python', 'Java')
nik_kap.increment_login_attempts()
nik_kap.increment_login_attempts()
nik_kap.increment_login_attempts()
nik_kap.reset_login_attempts()