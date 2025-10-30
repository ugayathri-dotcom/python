def add():
    l=[]
    n=int(input("enter no of elements"))
    s=0
    for i in range(n) :
          val=int(input("Enter values"))
          s+=val
    print("Sum of values",s)
    return s

add()
