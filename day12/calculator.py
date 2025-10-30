def add(a,b):
    c=a+b
    return c
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b!=0:
        return a/b
        
    
def calculator():
    print("Simple calulator")
    print(f"****1.Addition ***","****2.Subtraction****", "****3.Multiply***","4.Divide")

    ch=int(input("Enter the operation:1/2/3/4"))
    n1=float(input("Enter 1st number"))
    n2=float(input("Enter 2nd number"))

    if ch==1:
        print("Result:",add(n1,n2))
    elif ch==2:
        print("Result:",subtract(n1,n2))
    elif ch==3:
        print("Result:",multiply(n1,n2))
    elif ch==4:
        print("Result:",divide(n1,n2))
    else:
        print("Enter a valid number")

calculator()
          
