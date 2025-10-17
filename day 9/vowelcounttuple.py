l=()
l1=list(l)
count=0
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter the Characters")
    l1.append(val)

for j in l1:
    if (j =='a' or j=='e' or j=='o' or j=='u' or j=='i'):
        count+=1
    else:
        pass
print(tuple(l1))
print("No of vowels in tuple",count)
