a=[]
n=int(input("Enter no of elemnts"))
for i in range(n):
    val=int(input("Enter value"))
    a.append(val)
    
print('Created list',a)
for j in a[:]:
    if j%2 == 0:
        a.remove(j)
print("New list",a)
