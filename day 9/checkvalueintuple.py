l=()
b=list(l)
n=int(input("Enter no of elements"))
for i in range(n):
    val=input("Enter the elements")
    b.append(val)
l= tuple(b)
print("tuble elements",l)
a=input("enter the value to check")
if a in l:
     print("The value is present")
else:
    print("the value not present")

