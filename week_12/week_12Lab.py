#1
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b
    def __str__(self):
        return f'{self.a}x + {self.b}y'

vector1 = Vector(3,4)
vector2= Vector(3,4)
print('Is V1 and V2 the same?')
print(vector1 == vector2)
print(vector1)
#2
class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def distance(self, other):
        return ((self.x - other.x) **2 + (self.y - other.y) **2) **1/2
    def __str__(self):
        return f'the point is {self.x},{self.y}'
    
p1 = Point(3,4)
p2 = Point(3,4)
print(p1)
print(p2)
print(p1 == p2)






'''
#5
class RGBColor:
    #Each parameter (0-255)
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
    def __add(self, otherColor):
        color3 = RGBColor(0,0,0)
        self.r = (self.r + otherColor.r) /2
        self.g = (self.r + otherColor.g) /2
        self.b = (self.b + otherColor.b) /2
    
    def __str__(self):
        return f'RGB Value: ({self.r}, {self.g}, {self.b})'
    
c1 = RGBColor(170,150,200)
c2 = RGBColor(30,100,60)
c3 = c1 + c2

print('Color 1 =',c1)
print('Color 2 =',c2)
print('Color 3 =',c3)

'''

