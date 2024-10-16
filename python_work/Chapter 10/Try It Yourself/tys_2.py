# 10-3 Guest
guest_name = input('Please write your name: ')
filename = 'guest.txt'

with open(f'text_files/{filename}', 'w') as file_object:
    file_object.write(guest_name)

print('\n--------\n')

# 10-4 Guest Book
active = True
with open(f'text_files/{filename}', 'w') as file_object:
    while active:
        guest_name = input('Please write your name (press "q" to quit): ')
        if guest_name == 'q':
            active = False
        else:
            file_object.write(f"{guest_name}\n")

print("\n-------\n")

#10-5 Programming Poll
filename = "programming_poll.txt"
with open(f"text_files/{filename}", "w") as file_object:
    while True:
        name = input('Please enter your name (press "q" to quit): ')
        why = input('Now tell us why you like programming (press "q" to quit): ')
        if name == 'q' or why == 'q':
            break
        else:
            file_object.write(f"{name} likes programming because {why}.\n")
