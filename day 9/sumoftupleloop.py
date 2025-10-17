l=()
l1=list(l)
sum=0
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter the elements"))
    l1.append(val)
    sum=sum+val
l=tuple(l1)
print("Tuble is",l)
print("Sum of tuple",sum)
