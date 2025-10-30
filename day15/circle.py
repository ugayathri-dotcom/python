import math
class circle:
    def area(self):
        a=r*r*(math.pi)
        return a
    def peri(self):
        p=2*r*(math.pi)
        return p
        
r=int(input("Enter radius of cicle"))
r2=circle()
print("Area of a circle",r2.area())
print("Perimeter of a circle",r2.peri())

        
