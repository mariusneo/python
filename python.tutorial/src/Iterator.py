s = 'abc'
it = iter(s)

print(it.next())
print(it.next())
print(it.next())

print(it.next()) # this method call will raise an StopIteration error