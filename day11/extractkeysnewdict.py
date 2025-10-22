d={}
d1={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=input("Enter value")
    d[key]=val
    
print("Created dictionary",d)

d1=d.keys()
print("New dictionary after extracting keys from old dict",d1)
