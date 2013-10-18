'''
    Implementation of the popular path finding algorithm a* (a-star) search
    
    Algorithm is based on the explanations provided on the website :
    http://www.policyalmanac.org/games/aStarTutorial.htm
'''


class Square:
    def __init__(self, i, j):
        self._i = i
        self._j = j
        self._gcost = 0
        self._hcost = 0
        self._parent = None
       
    @property    
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, value):
        self._parent = value

    @property
    def i(self):
        return self._i
    @i.setter
    def i(self, value):
        self._i = value

    @property
    def j(self):
        return self._j
    @j.setter
    def setj(self, value):
        self._j = value

    @property
    def gcost(self):
        return self._gcost
    @gcost.setter
    def gcost(self, value):
        self._gcost = value

    @property
    def hcost(self):
        return self._hcost
    @hcost.setter
    def hcost(self, value):
        self._hcost = value


    def __hash__(self):
        return hash((self._i, self._j))

    def __eq__(self, other):
        return (self._i, self._j) == (other._i, other._j)
            
        
    def __str__(self):
        strSquare = '[i =' + str(self._i) + ', j='+str(self._j) + ', gcost=' +str(self.gcost) + ', hcost = ' + str(self.hcost)
        if not self._parent is None:
            strSquare +=', parent[i='+str(self._parent.i) + ', j=' + str(self._parent.j)+']'  
        
        strSquare += ']'   
        return strSquare

def hcost(i, j, desti, destj):
    return abs(desti - i ) * 10 + abs(destj - j) * 10;


def add_to_openlist(openlist, closedlist, m, currentSquare, i, j, distance, desti, destj ):
    if m[i][j] != -1:
        # only square which are not obstacles are taken into account
        square = Square(i, j)
        if square not in closedlist: 
            if square in openlist:
                index = openlist.index(square)
                square = openlist[index]
                if currentSquare.gcost + distance < square.gcost:
                    # a shorter path was found
                    square.parent = currentSquare
                    square.gcost = currentSquare.gcost + distance
            else:
                square.gcost = currentSquare.gcost + distance
                square.hcost = hcost(i, j, desti, destj)
                square.parent = currentSquare
                openlist.append(square)        
                            
                        
                        
def astar(m, starti, startj, desti, destj):
    openlist = []
    closedlist = []
    
    startSquare = Square(starti, startj)
    startSquare.hcost = hcost(starti, startj, desti, destj)
    openlist.append(startSquare)
    
    destinationFound = False
    currentSquare = None
    
    distance = 10
    diagonal_distance = 14
    while True:
        if len(openlist) == 0:
            # there are no more nodes to investigate, no path to destination was found
            break
        currentSquare = openlist[0]        
        for i in range (1, len(openlist)):
            square = openlist[i]
            #FIXME use a priority queue instead
            if currentSquare.gcost + currentSquare.hcost > square.gcost + square.hcost:
                currentSquare = square
        
        # switch currentSquare from openlist to closelist
        openlist.remove(currentSquare)    
        closedlist.append(currentSquare)   
            
        if currentSquare.i == desti and currentSquare.j == destj:
            # path to the destination was found
            destinationFound = True            
            break;
        
        
        # retrieve the adjacent nodes and add them to the open list
        # . . .
        # . x .
        # . . .
        if currentSquare.j > 0:
                if currentSquare.i > 0:
                    if m[currentSquare.i-1][currentSquare.j] != -1 and m[currentSquare.i][currentSquare.j -1] != -1:
                        # avoid doing diagonal steps next to the obstacles (when going upwards-back on the diagonal)
                        # . | 
                        # | x                         
                        add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i-1 , currentSquare.j-1, diagonal_distance, desti, destj)
                add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i , currentSquare.j-1, distance, desti, destj)
                if currentSquare.i < len(m) -1:
                        if m[currentSquare.i+1] [currentSquare.j] != -1 and  m[currentSquare.i] [currentSquare.j - 1] != -1:
                            add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i+1 , currentSquare.j-1, diagonal_distance, desti, destj)
                             
        if currentSquare.i > 0:
            add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i-1 , currentSquare.j, distance, desti, destj)
            if currentSquare.i < len(m) -1:
                add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i+1 , currentSquare.j, distance, desti, destj)
                
        if currentSquare.j < len(m[0]) -1 :
            if currentSquare.i > 0 :
                if m[currentSquare.i -1][currentSquare.j] != -1 and m[currentSquare.i][currentSquare.j+1] != -1:
                    add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i -1 , currentSquare.j+1, diagonal_distance, desti, destj)
            add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i , currentSquare.j+1, distance, desti, destj)
            if currentSquare.i < len(m) -1:
                if m[currentSquare.i+1][currentSquare.j] != -1 and m[currentSquare.i][currentSquare.j+1] != -1:    
                    add_to_openlist(openlist, closedlist, m, currentSquare, currentSquare.i+1 , currentSquare.j+1, diagonal_distance, desti, destj)
    
    path = []
    
    if destinationFound:        
        while True:
            path.append(currentSquare)
            if currentSquare == startSquare:
                break
            currentSquare = currentSquare.parent
        path.reverse()
    return path        

# Create a 8x6 matrix containing the terrain
# Having a value -1 in the matrix means that there is an obstacle
m = [[0 for x in range(8)] for x in range(6)]
m[0][4] = -1
m[1][4] = -1
m[2][4] = -1
m[3][4] = -1
m[3][6] = -1

starti, startj = 0,0 
desti, destj = 2,7

path = astar(m, starti, startj, desti, destj)

for square in path:
    print square
    
print 
print '-' * 50   
print
    
for i in range(len(m)):
    for j in range(len(m[0])):
        if i == starti and j == startj :
            print '{0:5}'.format('S'),
        elif i == desti and j == destj:            
            print '{0:5}'.format('D'),            
        elif m[i][j] == -1:
            print '|'*5,
        else:
            square = Square(i,j) 
            if square in path:        
                index = path.index(square)
                square = path[index]
                print '{0:5}'.format(str(square.gcost)),
            else:
                print '{0:5}'.format('.'),
    print

