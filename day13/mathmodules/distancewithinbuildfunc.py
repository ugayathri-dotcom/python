from math import*
a=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=float(input("Enter value"))
    a.append(val)
print("Created list1",a)
a1=[]
n1=int(input("Enter no of elements"))
for j in range(n1):
    val1=float(input("Enter value"))
    a1.append(val1)
print("Created list2",a1)
if len(a)!=len(a1):
    print ("Both list must be in same length")
else:
    distance=[]
    for i in range(len(a)):
        dist_val=dist([a[i]],[a1[i]])
        distance.append(dist_val)
    print("distance with inbuild dist function",distance)
