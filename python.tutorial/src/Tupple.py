t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# tuples may be nested
u = t, (1,2,3,4,5)
print u

# tuples are immutable, but they can contain mutable objects
v = ([1,2,3],[3,2,1])
print v


empty = ()
singleton = 'hello', #<-- note trailing comma
print len(empty)
print len(singleton)
print singleton


x,y,z = t
print x
print y
print z