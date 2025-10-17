l=()
l1=list(l)
mul=1
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter the elements"))
    l1.append(val)
    mul=mul*val
l=tuple(l1)
print("Tuble is",l)
print("Multiplication of tuple",mul)
