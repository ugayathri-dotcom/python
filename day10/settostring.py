s=set()
n=int(input("enter the no of elements"))
for i in range (n):
    val=input("Enter the value")
    s.add(val)
print("Created set1 is:",s)
b=''.join(s)
print("Set to string",b)
