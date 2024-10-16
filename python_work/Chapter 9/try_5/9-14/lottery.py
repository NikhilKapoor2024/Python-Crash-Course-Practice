from random import choice

lotto_nums = range(0, 10)
lotto_letts = ['A', 'B', 'C', 'D', 'E']

my_ticket = f"{choice(lotto_nums)}-{choice(lotto_letts)}"
count = 0

while 1:
    winning_ticket = f"{choice(lotto_nums)}-{choice(lotto_letts)}"
    print(f"Today's winning ticket is...'{winning_ticket}!")
    
    if my_ticket == winning_ticket:
        break
    else:
        count += 1

print(f"Congratulations, sir! You win with ticket # {my_ticket}!!!\n")
print(f"Number of loops: {count}")