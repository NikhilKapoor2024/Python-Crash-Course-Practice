"""A module with a class for dice."""
from random import randint

class Dice:
    """
    A module representing a dice.
    """

    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_dice(self):
        print(f"Rolling {self.sides}-sided dice...\n")
        result = randint(1, self.sides)
        print(f"You rolled a {result}!\n")

six_dice = Dice(12)
count = 0
while count < 10:
    six_dice.roll_dice()
    count += 1