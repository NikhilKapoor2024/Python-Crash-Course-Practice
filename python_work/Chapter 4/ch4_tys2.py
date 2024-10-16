#4-3 Counting to Twenty
numbers = list(range(1, 21))
print(numbers)

#4-4 One Million
numbers = list(range(1, 1_000_001))
# for number in numbers:
#    print(number)

#4-5 Summing a Million
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6 Odd Numbers
odd_numbers = list(range(1, 21, 2))
for odd_number in odd_numbers:
    print(odd_number)

#4-7 Threes
threes = []
for value in range(3, 30):
    three = value * 3
    threes.append(three)

print(threes)

#4-8 Cubes
cubes = []
for value in range(1, 11):
    cube = value ** 3
    print(cube)
    cubes.append(cube)

#4-9 Cube Comprehension
comp_cube = [value ** 3 for value in range(1, 11)]
print(comp_cube)

#4-10 Slices
print("The first three items in the list are:")
for number in numbers[:3]:
    print(number)

print("The three items in the middle of the list are:")
for number in numbers[10:13]:
    print(number)

print("The last three items in the list are:")
for number in numbers[-3:]:
    print(number)

# 4-11 My Pizzas, Your Pizzas
pizzas = ['Brooklyn', 'Chicago-Style', 'Hawaiin']
friend_pizzas = pizzas[:]

pizzas.append('Square')
friend_pizzas.append('Vegetarian')
print("My friend's favorite pizas are:")
for pizza in friend_pizzas:
    print(pizza)

#4-12 More Loops
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print("My friend copied my favorite foods!\nHere's a list of mine:")
for food in my_foods:
    print(food)
print("\nAnd here are my friend's favorite foods:")
for food in friends_foods:
    print(food)
print("\nThey're exactly the same, see!?")
