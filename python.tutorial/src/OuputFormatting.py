s = 'Hello world!'
print str(s)

print repr(s)

print str(1.0 / 7.0)

print repr(1.0 / 7.0)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print s


# write tables and cubes
for x in range(1, 11):
    print repr(x).rjust(2), repr(x * x).rjust(3),
    print repr(x ** 3).rjust(4)
    
print '-' * 50
    
for x in range(1, 11):
    print '{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x)    
    
print '-' * 50
    
print '12'.zfill(5)    

print 'We are the {} who say "{}"!'.format('knights', 'Ni')
print 'We are the {0} who say "{1}"!'.format('knights', 'Ni')

print 'This {food} is {adjective}.'.format(food='spam', adjective='absolutely terrible')

print 'The story of {}, {} and {other}'.format('Bill', 'John', other='Lonely Bob')

import math
print 'The value of PI is approximately {0:.3f}.'.format(math.pi)

table = {'Sjoerd':4127, 'Jack':4098, 'Dcab':7687}
for name, phone in table.items():
    print '{0:10} ==> {1:10d}'.format(name, phone) 