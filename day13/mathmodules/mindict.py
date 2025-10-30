from math import*
d={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=input("Enter value")
    d[key]=val
    
print("Created dictionary",d)
m=min(d)
print("Minimum value in dictionary",m)
