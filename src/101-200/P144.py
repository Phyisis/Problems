from helpers import analytics, primes
from helpers.vector import vec2d,ray2d
analytics.monitor()
from fractions import Fraction

"""
ellipse:    4x^2 + y^2 = 100
            x^2/5^2 + y^2/10^2 = 1
slope at x,y: -4x/y
p0 = 0,10.1
p1 = 1.4,-9.6

4*v.x^2 + v.y^2 == 100
v = p+tu
4*(p.x+t*u.x)^2 + (p.y+t*u.y)^2 == 100
"""

def intersectDistance(s):
    p,u = s.point,s.vector
    a = 1/(4*u.x**2+u.y**2)
    b = 2*p.x*p.y*u.x*u.y-(p.y**2-100)*u.x**2-(p.x**2-25)*u.y**2
    s1 = -a * (2*b**0.5 + 4*p.x*u.x + p.y*u.y)
    s2 = a * (2*b**0.5 - 4*p.x*u.x - p.y*u.y)
    return max(s1,s2)

def main():
    p0,p1 = vec2d(0,10.1),vec2d(1.4,-9.6)
    s = ray2d(p0,vec2d(p1.x-p0.x,p1.y-p0.y).toUnit())
    bounces = 0
    while abs(s.point.x)>0.01 or s.point.y < 0 or bounces == 0:
        d = intersectDistance(s) #distance to intersection
        p = s.pointAtDistance(d) #point of intersection
        n = vec2d(-10*p.x/5,-5*p.y/10).toUnit() #normal vector
        r = s.vector - n.scaleBy(2*n.dot(s.vector)) #reflection direction
        s = ray2d(p,r) #new ray
        bounces += 1
    return bounces-1

print(main(), analytics.lap(), analytics.maxMem())
# 354