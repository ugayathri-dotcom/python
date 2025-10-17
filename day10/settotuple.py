s=set()
n=int(input("enter the no of elements"))
for i in range (n):
    val=input("Enter the value")
    s.add(val)
print("Created set1 is:",s)
b=tuple(s)
print("Set to tuple",b)

s1=()
a=list(s1)
n1=int(input("enter the no of elements"))
for j in range (n1):
    val1=input("Enter the value")
    a.append(val1)
print("Created tuple is:",tuple(a))
s2=set(a)


print("tuple to set",s2)
