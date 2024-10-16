# 10-9 Count Words
try:
    with open('text_files/book.txt', 'r') as f:
        contents = f.read()
except FileNotFoundError:
    print("The file 'book.txt' was not found")
else:
    result = contents.lower().count('the')
    
    print(result)