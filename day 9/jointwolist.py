a=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter Value")
    a.append(val)
print(a)
b=[]
n1=int(input("Enter no of elements"))
for i in range(n1):
    val1=input("Enter Value")
    b.append(val1)
print(b)
a.extend(b)
print("After joining twolist",a)
