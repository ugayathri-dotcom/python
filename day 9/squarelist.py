a=[]
b=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter value"))
    a.insert(i,val)
print("Created list",a)
for j in a:
    s=j*j
    b.append(s)
print("Square of list:",b)  
       


