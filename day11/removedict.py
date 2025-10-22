d={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=input("Enter value")
    d[key]=val
    
print("Created dictionary",d)
a=input("Enter a key to remove")
d.pop(a)
print("after removing key",d)
