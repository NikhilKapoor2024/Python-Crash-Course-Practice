"""A module representing functions for accounts in multiple classes."""

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

class Priveleges:
    """class for priveleges for admin"""
    def __init__(self, commands=['can add post', 'can delete post']):
        self.commands = commands
    
    def show_priveleges(self):
        print("The following priveleges are available to the admin:")
        for command in self.commands:
            print(f"- {command}")

class Admin(User):
    """child class of User"""

    def __init__(self, first_name, last_name, likes, dislikes):
        super().__init__(first_name, last_name, likes, dislikes)
        self.priveleges = Priveleges()