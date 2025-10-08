import math
print("------Square------")
a=int(input("Enter side of a Square"))
sa= a**2
print("Area of a Sqaure",sa)
print("------Rectangle-------")
l=int(input("Enter Length ofRectangle"))
b=int(input("Enter Breath of Rectangle"))
ra=l*b
print("Area of Rectangle",ra)
print("-------Triangle-------")
b1=int(input("Enter Breath of Triangle"))
h=int(input("Enter Height of Triangle"))
ta=1/2 *(b*h)
print("Area of Triangle",ta)
print("------Trapexoid-----")
br1=int(input("Enter Breath1 of Trapexoid"))
br2=int(input("Enter Breath2 of Trapexoid"))
h1=int(input("Enter Height of Trapexoid"))
tra=((br1+br2)*h)*1/2
print("Area of Trapexoid",tra)
print("-------Circle-------")
r=int(input("Enter radius of circle"))
ca= (math.pi)*r*r
print("Area of Cirle", ca)
print("------Cylinder-----")
h2=int(input("Enter Height of Cylinder"))
r1=int(input("Enter radius of Cylinder"))
cya=(math.pi)*r1*r1*h2
print("Volume of Cylinder", cya)
print("------Cone------")
h3=int(input("Enter Height of Cone"))
r2=int(input("Enter radius of Cone"))
coa= 1/3*(math.pi)*r2*r2*h3
print("Volume of Cone", coa)
print("-------Sphere-------")
r3=int(input("Enter radius of Sphere"))
sa= 4/3*(math.pi)*r3*r3
print("Volume of Sphere", sa)












