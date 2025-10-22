d={}
s=1
n=int(input("Enter no of elements"))
for i in range(n):
    key=int(input("Enter key"))
    val=int(input("Enter value"))
    d[key]=val
    s*=val
    s*=key
print("Created dictionary1",d)

print("Multiplication of values and keys ",s)
