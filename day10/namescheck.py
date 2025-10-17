s=set()
n=int(input("enter the no of elements"))
for i in range (n):
    val=input("Enter the value")
    s.add(val)
print("Created set1 is:",s)
c=input("Enter a string to check")
if c in s:
    print(f"{c} is present in the set")
else:
    print(f"{c} not present in the set")
'''b=''.join(s)
print("Set to string",b)

c=input("Enter a string to check")
print(b.startswith(c))'''
