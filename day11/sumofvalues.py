d={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=int(input("Enter value"))
    d[key]=val
    
print("Created dictionary1",d)
s=sum(d.values())
print("Sum of values ",s)
