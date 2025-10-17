s=set()
s1=set()
count=0
n=int(input("enter the no of elements"))
for i in range (n):
    val=int(input("Enter the value"))
    s.add(val)
print("Created set1 is:",s)

for j in s:
    if j <= 1:
      continue
    count=0
    for k in range(2,j):
        if j % k == 0:
           count+=1
           break
    if count==0:
        s1.add(j)
        
print("Primes set",s1)
        
