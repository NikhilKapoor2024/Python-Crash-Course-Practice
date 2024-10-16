#5-8 Hello Admin
usernames = ['robfred2001', 's@llyf1elds', 'alphaomegabetasin', 'st0nez', 'admin']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")

#5-9 No Users
usernames = []
if username:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")

#5-10 Checking Usernames
current_users = ['sally', 'billy', 'joel', 'steven', 'harry', 'greg', 'robert']
new_users = ['billy', 'george', 'joel', 'sarah', 'vicky']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"'{new_user}' is already a current user. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

#5-11 Ordinal Numbers
ordinals = list(range(1, 10))
print(ordinals)
for num in ordinals:
    if num < 4:
        print(f"{num}st")
    else:
        print(f"{num}th")