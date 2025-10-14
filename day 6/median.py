a=int(input("Enter First value"))
b=int(input("Enter second value"))
c=int(input("Enter third value"))
if (a>b and a<c) or (a<b and a>c):
    print("Median Value is",a)
elif (b>a and b<c) or (b<a and b>c):
    print("Meidan value is",b)
else: print("Median value is",c)
