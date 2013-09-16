print(range(10))

print(range(5,10))

print(range(0,10,3))

print(range(-1, -5, -1))

print(range(-10,-100, -30))

# to iterate over the elements of an array the
# range and len functions can be combined
array = ['Mary', 'hat', 'a', 'little', 'lamb']
for i in range(len(array)):
    print i, array[i]
    