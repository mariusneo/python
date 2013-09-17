'''
Solution for the classical backpack problem to be solved with
"Greedy" technique. Problem : Having a series of <i>n</i> objects,
where the object <i>i</i> has the value <i>v(i)</i> and the weight
<i>w(i)</i> find out the most valuable combination of objects which can be
fit into a backpack with a capacity of <i>W</i> units.
'''
class Backpack:
    def  selectWares(self, backpackWeight, wares):
        swares = sorted(wares, key = lambda ware : ware.value+0.0/ware.weight)
        selected =[]
        availableWeight = backpackWeight 
        for ware in swares:
            if availableWeight == 0:
                break
            if availableWeight - ware.weight >=0:
                selected.append(ware)
                availableWeight = availableWeight - ware.weight                
                
        return selected
            
        
        
        


class Ware:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
    
    def __repr__(self):
        return '[weight : '+ str(self.weight) + ' value : ' + str(self.value) + ']'
    

ware1= Ware(10, 60)
ware2 = Ware(20, 100)
ware3 = Ware(30, 120)
wares = [ware1, ware2, ware3]

bp = Backpack()
selectedWares = bp.selectWares(50, wares)
print selectedWares  