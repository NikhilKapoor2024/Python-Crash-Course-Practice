# 8-12. Sandwiches:
def make_sandwich(*ingredients):
    for ingredient in ingredients:
        print(f"- {ingredient}")

print("\nThese are the ingredients going into your sandwich:")
make_sandwich('ham', 'cheese', 'lettuce', 'tomatoes')
print("\nThese are the ingredients going into your sandwich:")
make_sandwich('turkey', 'salami')
print("\nThese are the ingredients going into your sandwich:")
make_sandwich('chips', 'beef', 'provolone cheese')

# 8-13. User Profile:
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('nikhil', 'kapoor', age='23', likes='games')
print(user_profile)

# 8-14. Cars:
def build_car(manufacturer, model, **car_info):
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model
    return car_info

car = build_car('subaru', 'outback', color='blue', tow_package=True)
print(car)