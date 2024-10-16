#7-8 Deli
sandwhich_orders = ['ham', 'cheese', 'pastrami', 'tuna', 'pastrami', 'peanut butter', 'pastrami', 'jelly']
finished_orders = []

print("NOTE: We are out of pastrami.")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

print(f"List of sandwiches: {sandwhich_orders}")

while sandwhich_orders:
    order = sandwhich_orders.pop()
    finished_orders.append(order)
    print(f"I finished making your {order} sandwich.")

# 7-10 Dream Vacation
vacations = {}

active = True
while active:
    name = input("\nWhat is your name? ")
    vacation = input("What is your dream vacation? ")
    vacations[name] = vacation

    response = input("Would you like to continue? (enter 'yes' or 'no'): ")
    if response == 'no':
        active = False

print("\n-------- POLL RESULT --------")
for name, vacation in vacations.items():
    print(f"{name.title()} would love to take a vacation to {vacation.title()}.")
