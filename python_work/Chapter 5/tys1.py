#5-1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\n")

#5-2 More Conditional Tests
requested_color = 'red'
if requested_color != 'orange':
    print("Don't give me orange yet!")

print(car.title() == 'Subaru')

print(3 >= 1)
print(15 == 15)
print(20 > 100)

if 3 >= 1 and 4 <= 6:
    print("This conditional statement is correct")

rocks = ['mineral', 'rough', 'smooth']
print('mineral' in rocks)
print('subatomic' not in rocks)
