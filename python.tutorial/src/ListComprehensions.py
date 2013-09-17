squares = []
for x in range(10):
    squares.append(x * x)
print squares

# rewrite for a better readability
squares = [x ** 2 for x in range(10)]
print squares    

squares = map(lambda x : x ** 2, range(10))
print squares




combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if (x != y):
            combs.append((x, y))
print combs            

# concise rewriting of the routine above
diff = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print diff


vec = [-4, -2, 0, 2, 4]
doubles = [x * 2 for x in vec]
print doubles

positives = [x for x in vec if x >= 0]
print positives

absolutes = [abs(x) for x in vec]
print absolutes

freshfruit = ['   banana', '  loganberry', '   passion fruit  ']
strippedfruit = [fruit.strip() for fruit in freshfruit]

tuples1 = [(x, x ** 2) for x in range(6)]
print tuples1

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatlist = [num for elem in vec for num in elem]
print flatlist

# complex functions in list comprehension
from math import pi
approx = [str(round(pi, i)) for i in range(1, 6)]
print approx



# list comprehension can be applied on matrix as well
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
transposed = [[row[i] for row in matrix] for i in range(4)]
print transposed
#there can be a builtin function used for this purpose
transposed1 = zip(*matrix)
print(transposed1)
