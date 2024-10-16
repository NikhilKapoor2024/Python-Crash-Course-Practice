#3-4 Guest List
invites = ['Barack Obama', 'Abraham Lincoln', 'George Perez']
print(invites)

#3-5 Changing Guest List
print(f"Unfortunately, {invites[0]} couldn't make it")
invites[0] = 'Tom King'
print(invites)

#3-6 More Guests
invites.insert(0, 'Billy Bones')
invites.insert(1, 'Jane Doe')
invites.append('John Smith')
print(invites)

#3-7 Shrinking Guest List
print("Turns out I can only invite two people for dinner")
popped_guest = invites.pop(0)
print(f"I apologize, {popped_guest}, but you must leave.")
print(invites)
popped_guest = invites.pop(-1)
print(f"I apologize, {popped_guest}, but you must leave.")
print(invites)
popped_guest = invites.pop(2)
print(f"I apologize, {popped_guest}, but you must leave.")
print(invites)
popped_guest = invites.pop(0)
print(f"I apologize, {popped_guest}, but you must leave.")
print(invites)

print(f"Don't worry, {invites[0]}, {invites[1]}, you're still invited to dinner.")
del invites[0]
del invites[0]
print(invites)
