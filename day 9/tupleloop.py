l=()
l1=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter the elements")
    l1.append(val)
l=tuple(l1)
print("Tuble is",l)
