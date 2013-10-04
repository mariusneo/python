'''
7.6 Given a two dimensional graph with points on it, find a line
which passes the most number of points.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'Point[x=' + str(self.x) + ', y=' + str(self.y) + ']'

class Line:
    epsilon = 0.0001
    
    def __init__(self, point1, point2):
        
        if point1.x == point2.x:
            self.infiniteSlope = True
            self.slope = 0
            self.intercept = point1.x
        else:
            self.slope = (point1.y - point2.y)/(point1.x - point2.x)
            self.intercept = point1.y - self.slope * point1.x
            self.infiniteSlope = False
        
    def __hash__(self):
        return hash((self.slope, self.intercept))
    
    def __eq__(self, other):
        return  (self.slope - other.slope < Line.epsilon) and (self.intercept - other.intercept < Line.epsilon)
    
    def __str__(self):
        if self.infiniteSlope:
            return 'Line[infiniteSlope, intercept=' + str(self.intercept) + ']'
        else:
            return 'Line[slope =' + str(self.slope) + ', intercept=' + str(self.intercept) + ']'
    
points = [Point(1,1), Point(2,2), Point(3,3), Point(1,4), Point(1,5), Point(2,5)]    

lineMap ={}
maxPoints = 0
bestLine = None
for i in range(len(points)):
    for j in range(i+1, len(points)):
        line = Line(points[i], points[j])
        if (lineMap.has_key(line)):
            lineMap[line] = lineMap[line]+1
        else:
            lineMap[line] = 1
        if lineMap[line] > maxPoints:
            bestLine = line
            maxPoints = lineMap[line]
            
print bestLine
print lineMap[bestLine]