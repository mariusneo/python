class MyClass2:
    def __init__(self):
        pass
    
    
x = MyClass2()
x.counter =1
while x.counter < 10:
    x.counter = x.counter * 2
print x.counter

del x.counter        