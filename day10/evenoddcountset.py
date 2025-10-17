l=set()
l1=set()
l2=set()

n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter the elements"))
    l.add(val)
print("created set is",l)
count=0
c=0
for j in l:
    if j % 2 != 0:  #odd
        l1.add(j)
        count+=1
    else:
        l2.add(j)
        c+=1
        
print("Odd numbers in set",l1)
print("The no odd's in set",count)
print("Even numbers in set",l2)
print("The no even's in set",c)
