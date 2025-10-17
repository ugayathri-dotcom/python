l=set()
l1=set()

n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter the elements"))
    l.add(val)
print("created set is",l)

for j in l:
    if j>1:
        sum=0
        for k in range(1,j):
            if j%k==0:
                sum+=k
        if sum == j:
            l1.add(j)
    
print("The perfect no set",l1)
