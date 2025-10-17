a=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter Value")
    a.append(val)
print("list 1",a)
b=[]
n1=int(input("Enter no of elements"))
for i in range(n1):
    val1=input("Enter Value")
    b.append(val1)
print("List 2",b)
d=set(a).symmetric_difference(b)
d1=list(d)
print("difference",d1)

