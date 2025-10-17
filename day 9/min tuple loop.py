l=()
a=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter value"))
    a.insert(i,val)
#print("Created list",a)
b=sorted(a)
#print("After sorting",b)
min=b[0]
max=b[-1]

print("Created tuple",tuple(a))
print("Minimum value",min)
print("Maximum value",max)

