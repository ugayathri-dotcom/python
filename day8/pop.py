a=[]
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter Value")
    a.append(val)
print('Created list',a)
a.pop(-1)    #to remove last element
print("After deletion",a)
