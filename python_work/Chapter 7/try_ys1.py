#7-1 Rental Car
car = input("What car are you looking for? ")
print(f"I'll see if I can find you a {car.title()}")

#7-2. Restaurant Seating
num_guests = input("\nHello. How many guests would you like to be seated? ")
num_guests = int(num_guests)
if num_guests > 8:
    print("Unfortunetly, we cannot seat that many guests.")
else:
    print("Of course! Right this way, sir.")

# 7-3. Multiples of Ten
num = input("\nType in a number: ")
num = int(num)
if num % 10 != 0:
    print(f"{num} isn't a multiple of 10!")
else:
    print(f"{num} is a multiple of 10.")