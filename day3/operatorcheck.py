a=int(input("Enter No1"))
b=int(input("Enter No2"))
op=input("Enter Operator(+_, -, *, /):")
if op == '+':
    r= a+b
    print("Addition:",r)
elif op == '-':
    r=a-b
    print("Subraction:",r)
elif op == '*':
    r=a*b
    print("Product:",r)
elif op == '/':
    r=a/b
    print("Division:",r)
else: print("invalid operator")
