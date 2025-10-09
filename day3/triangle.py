a=int(input("Enter A value"))
b=int(input("Enter B value"))
c=int(input("Enetr C value"))

if a == b and a == c:
    print("Equilateral Triangle")
elif a == b or a == c or b == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

    
