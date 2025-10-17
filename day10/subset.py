s=set()
n=int(input("enter the no of elements"))
for i in range (n):
    val=input("Enter the value")
    s.add(val)
print("Created set1 is:",s)
s1=set()
n1=int(input("enter the no of elements"))
for j in range (n1):
    val1=input("Enter the value")
    s1.add(val1)
print("Created set2 is:",s1)
print(f"{s} is a subset of {s1}",s.issubset(s1))
