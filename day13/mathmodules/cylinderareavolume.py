import math
r=float(input("enter the radius of cylinder"))
h=float(input("enter height of cylinder"))
a=2*(math.pi)*r*(h+r)
v=h*r*r*math.pi
print("Area of cylinder",a)
print("volume of cylinder",v)
