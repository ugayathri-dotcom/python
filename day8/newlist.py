a=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter value")
    a.append(val)
print('Created list',a)

n1=int(input("enter no of elements to be added again"))
for j in range(n1):
    val1=input("Enter new values to be added")
    a.append(val1)
print("New list",a) 
