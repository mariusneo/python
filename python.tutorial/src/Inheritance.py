class BaseClassName:
    def __init__(self):
        print "BaseClassName ctor called"
        pass
    
class DerivedClassName(BaseClassName):
    def __init__(self):    
        print "DerivedClassName ctor called"


x = DerivedClassName()        


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
        
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
            
    _update = update # private copy of the original update() method
    
class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update method,
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)     