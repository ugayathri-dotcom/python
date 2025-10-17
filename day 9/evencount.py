a=[]
count=0
c=0
sumeven=0
sumodd=0
n=int(input("Enter no of elements"))
for i in range(n):
    val=int(input("Enter value"))
    a.insert(i,val)
print("Created list",a)
for i in a:

    if i%2==0:
        count+=1
        sumeven=sumeven+i
    else:
       c+=1
       sumodd=sumodd+i
print("No of even numbers",count)
print("No of odd numbers",c)
print("Sum of even nos",sumeven,"Sum of odd no",sumodd)
