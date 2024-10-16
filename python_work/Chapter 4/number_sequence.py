# lists of squares
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# fibonacci sequence
fibn = []
fibn.append(0)
fibn.append(1)
n = 2
for value in range(1, 15):
    if n < 15:
        fibn.append((fibn[n - 2] + fibn[n - 1]))
    n = n + 1

print(fibn)