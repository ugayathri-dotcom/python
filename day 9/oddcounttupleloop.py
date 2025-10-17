l=()
l1=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter the elements"))
    l1.append(val)
l=tuple(l1)
print("Tuble is",l)
l2=list(l)
l3=[]
count=0
for j in l:
    if j % 2 != 0:
        l3.append(j)
        count+=1
    else:
        pass
print("Odd numbers in tuple",tuple(l3))
print("The no odd's in tuple",count)
