# 10-1 Learning Python
file_path = 'text_files/learning_python.txt'

print("1. Read entire File")
with open(file_path) as file_object:
    contents = file_object.read()

print(contents)

print("\n2: Read Line by Line")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\n3. Store Lines in a List')
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("\n")
#10-2 Learning C
for line in lines:
    print(line.replace('Python', 'C').rstrip())