d={}
d1={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=input("Enter value")
    d[key]=val
    
print("Created dictionary",d)
a=input("Default key ")
b=input("Default value for key")
d.setdefault(a,b)
print("Value of the key",d)
