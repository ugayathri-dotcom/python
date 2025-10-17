l=()
l1=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter the elements")
    l1.append(val)
l=tuple(l1)
print("Tuble 1 is",l)
t=()
l2=list(t)
n1=int(input("Enter no of elements"))
for i in range(n1):
    val1=input("Enter the elements")
    l2.append(val1)
t=tuple(l2)
print("Tuble 2 is",t)
c=()
c=l+t
print("After concatenation",c)
