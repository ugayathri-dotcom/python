l=()
l1=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter the elements"))
    if val % 2 == 0:
       l1.append(val)
l=tuple(l1)
print("Tuble is",l)
'''l2=list(l)
for j in l:
    if j % 2 == 0:
        l2.append(j)
    else:
        pass

print(tuple(l2))'''

        
