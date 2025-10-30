import math
a=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter value"))
    a.insert(i,val)
print("Created list",a)
m=max(a)
m1=min(a)

print("Minimum value",m1)
print("Maximum value",m)

