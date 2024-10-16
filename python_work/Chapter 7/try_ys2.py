#7-4. Pizza Toppings
msg = ""
prompt = "What topping would you like on your pizza?"
prompt += "\n(Enter 'quit' to exit): "
while msg != 'quit':
    msg = input(prompt)
    if msg == 'quit':
        break
    else:
        output = f"We'll add {msg} to your pizza, sir.\n"
        print(f"{output}")

#7-5. Movie Tickets
prompt = "Enter your age here\n(Enter 'quit' to exit): "
age = ""
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Ticket Price: Free")
        elif age >= 3 and age < 12:
            print("Ticket price: $10")
        elif age >= 12:
            print("Ticket price: $15")

#7-6. Three Exits
active = True
prompt = "Hello, what's your name?"
prompt += "\n(Enter quit to exit): "
while active:
    name = input(prompt)
    if name == 'quit':
        active = False
        break
    else:
        output = f"Ah, hello {name.title()}!\n"
        print(output)

#7-7. Infinity
active = True
while active:
    print("This is an infinite loop!")