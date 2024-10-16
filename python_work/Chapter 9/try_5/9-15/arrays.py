import array

first_arr = array.array('b', range(1, 4))
print("This is my array: ", first_arr)
while first_arr:
    print(first_arr.pop())

s = b'This is an array.'
a = array.array('b', s)
print("This is a byte string: ", s)
print("This is that byte string as an array: ", a)