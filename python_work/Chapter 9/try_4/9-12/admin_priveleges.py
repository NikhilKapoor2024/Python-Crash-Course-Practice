"""A module that has privelges and admin accounts represented as classes."""
from users import User

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