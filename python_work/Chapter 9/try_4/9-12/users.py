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