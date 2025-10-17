l=()
l1=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter the elements")
    val1=val.upper()
    l1.append(val1)
print(tuple(l1))
