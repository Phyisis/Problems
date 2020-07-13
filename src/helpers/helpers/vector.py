from math import acos

class vec2d():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")" 
    
    def __add__(self,V):
        return vec2d(self.x+V.x,self.y+V.y)
    
    def __sub__(self,V):
        return vec2d(self.x-V.x,self.y-V.y)

    def magnitude(self):
        return (self.x**2+self.y**2)**0.5

    def dot(self,U):
        return self.x*U.x+self.y*U.y
    
    def scaleBy(self,s):
        return vec2d(self.x*s,self.y*s)
    
    def angleFrom(self,U):
        return acos(self.dot(U)/(self.magnitude()*U.magnitude()))

    def toUnit(self):
        return self.scaleBy(1/self.magnitude())

class ray2d():
    def __init__(self,point,vector):
        self.point = point
        self.vector = vector
    
    def __str__(self):
        return "(" + self.point.__str__() + "," + self.vector.__str__() + ")"
    
    def pointAtDistance(self,d):
        return self.point + self.vector.toUnit().scaleBy(d)