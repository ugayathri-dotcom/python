a=[]
n=int(input("Enter no of Cities"))
for i in range(n):
    val=input("Enter City name")
    a.append(val)
print('Created list',a)
b=input("enter the city name to remove city")
a.remove(b)
print("After removal",a)
c=input("enter the city to add")
a.append(c)
print("After adding",a)
