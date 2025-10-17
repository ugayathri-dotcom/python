s=set()
n=int(input("enter the no of elements"))
for i in range (n):
    val=input("Enter the value")
    s.add(val)
print("Created set is:",s)
b=input("Enter the value to remove")
s.remove(b)
print(f"After removal of {b} New set:",s)
