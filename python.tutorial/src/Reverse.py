class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index -1
        return self.data[self.index]
    

rev = Reverse('spam')

print iter(rev)

for char in rev:
    print char,    
   
print
print '*' * 50   
   
def strreverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
        
for char in strreverse('golf'):
    print char,                 