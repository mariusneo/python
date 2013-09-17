mygenerator = (x*x for x in range(3))

for i in mygenerator:
    print i

# once iterated, the elements of the generator are forgotten 
for i in mygenerator:
    print i

print '-' * 50

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        
agenerator = createGenerator()
for i in agenerator:
    print i