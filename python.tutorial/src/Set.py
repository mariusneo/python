basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
fruits = set(basket)
print fruits
print 'orange' in fruits
print 'crabgrass' in fruits


a = set('abracadabra')
b = set('alacazam')
print a
print a-b #letters in a, but not in b
print a|b #letters in a or b
print a&b #letters in both a and b
print a^b # letters in a or b, but not in both XOR

aset = {x for x in 'abracadabra' if x not in 'abc'}
print aset