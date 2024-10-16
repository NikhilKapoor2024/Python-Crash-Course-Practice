#3-8 Seeing the World
places = ['Seattle', 'Toledo', 'London', 'Tokyo', 'Queens']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse = True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9 Dinner Guests
invites = ['Barack Obama', 'Abraham Lincoln', 'George Perez']
print(len(invites))

#3-10 Every Function
groceries = ['Bananas', 'Shampoo', 'Toothbrushes', 'Juices', 'Lemons', 'Eggs', 'Yogurt']
print(f"These are the lists of groceries to get: {groceries}")
groceries.sort()
print(f"If you need the list in alphabetical order: {groceries}")
hot_item = groceries.pop(2)
print(f"The one item to look for is {hot_item}")
print(f"Now that you got the {hot_item}, all that's left are {sorted(groceries, reverse=True)}")
print("Now you just need to find...oh here we go!")
item_to_rmv = 'Shampoo'
groceries.remove(item_to_rmv)
print(f"With the item found, all that's left are {groceries}")
print("Oops, forgot to include 'Peanuts' on the list!")
groceries.append('Peanuts')
print(f"Now the list should say {sorted(groceries)}")

#3-11 Intentional Error
print(groceries[7])