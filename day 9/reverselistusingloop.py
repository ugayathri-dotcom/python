a=[]
sum=0
r=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter value"))
    a.insert(i,val)
print("Created list",a)
for j in range(n-1,-1,-1):
    r.append(a[j])
print("Reversed list is:",r)



