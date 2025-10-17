l=()
l1=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter the elements")
    l1.append(val)
l=tuple(l1)
print("Tuble 1 is",l)
a=input("Enter the value to find value's count and its index")
print("The count of given value is",l.count(a))
print("The index of given value",l.index(a))


        
