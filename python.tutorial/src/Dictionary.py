tel = {'jack':4098, 'sape':4139}
tel['guido'] = 4127
print tel
print tel['jack']

del tel['sape']

tel['irv'] = 4127
print tel

print tel.keys()

print 'guido' in tel

#print tel['marius'] # wouldn't work because there's no mapping for 'marius' key

tel1 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print tel1 

#dict comprehensions
cubes = {x:x**3 for x in (2,4,6)}
print cubes

tel2 = dict(sape=4139, guido=4127, jack=4098)
print tel2