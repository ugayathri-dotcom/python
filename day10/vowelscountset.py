l=set()
l1=set()
count=0
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter the Characters")
    l.add(val)
print("Created set",l)

for j in l:
    if (j =='a' or j=='e' or j=='o' or j=='u' or j=='i'):
        count+=1
        l1.add(j)
    else:
        pass
#print(tuple(l1))
print("No of vowels in set",count)
print("vowels",l1)
