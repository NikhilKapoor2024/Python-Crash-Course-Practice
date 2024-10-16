# 8-15. Printing Models:
import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

# 8-16. Imports:
import profile_function as pf

# user_profile = profile_function.build_profile('nikhil', 'kapoor', location='here', time='when')
# user_profile = build_profile('nikhil', 'kapoor', location='here', time='now')
user_profile = pf.build_profile('nikhil', 'kapoor', location='here', time='now')

print(f"{user_profile}")

