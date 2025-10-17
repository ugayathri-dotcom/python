a=[]
b=0
#sum=0
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter value"))
    a.insert(i,val)
print("Created list",a)
b=sum(a)
print("sum of list",b)
'''for i in a:
    sum=sum+i
print("Sum of list",sum)'''
