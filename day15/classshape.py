import math
class shape:
    class circle:
        def area(self,r):
            a=r*r*(math.pi)
            return a
        def peri(self,r):
            p=2*r*(math.pi)
            return p
    class triangle:
        def area(self,b,h):
            at=0.5*b*h
            return at
        def peri(self,a,b,c):
            pt=a+b+c
            return pt
    class square:
        def area(self,a):
            sa=a*a
            return sa
        def peri(self,a):
            ps=4*a
            return ps
                   
r=int(input("Enter radius of circle"))
r2=shape.circle()
print("Area of a circle",r2.area(r))
print("Perimeter of a circle",r2.peri(r))
b=int(input("enter base of triangle"))
h=int(input("enter height of triangle"))
a1=int(input("enter side1 of trianle"))
a2=int(input("enter side2 of trianle"))
t=shape.triangle()
print("Area of triangle",t.area(b,h))
print("Perimeter of triangle",t.peri(b,a1,a2))
a=int(input("enter a side of square"))
s=shape.square()
print("area of square",s.area(a))
print("Perimeter of square",s.peri(a))




