d={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=input("Enter value")
    d[key]=val
print("Created dictionary1",d)
d1={}
n1=int(input("Enter no of elements"))
for j in range(n1):
    key1=input("Enter key")
    val1=input("Enter value")
    d[key1]=val1   
print("Created dictionary2",d1)
d.update(d1)
print("Merged dictionaries",d)
