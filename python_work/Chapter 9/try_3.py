# 9-6. Ice Cream Stand:
class Restaurant:
    """class representation of a restaurant"""
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The {self.name} serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"{self.name} is now open!\n")

class IceCreamStand(Restaurant):
    """class representation of an ice cream stand"""
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'oreo', 'strawberry']
    
    def list_flavors(self):
        print("We have the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

dessert_place = IceCreamStand('Sahara Dessert', 'ice cream')
dessert_place.describe_restaurant()
dessert_place.list_flavors()

# 9-7. Admin:
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

admin_jake = Admin('Jake', 'Jambori', 'being an admin', 'not being an admin')
admin_jake.describe_user()
admin_jake.priveleges.show_priveleges()

# 9-9: Battery Upgrade
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Represent aspects of a car, specific to eletric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()
    
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.battery.get_range())
my_tesla.battery.upgrade_battery()
print(my_tesla.battery.get_range())