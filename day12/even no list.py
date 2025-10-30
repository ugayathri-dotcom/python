def add():
    l=[]
    n=int(input("enter no of elements"))
   
    for i in range(n) :
          val=int(input("Enter values"))
          if val%2==0:
              l.append(val)
    print("Even no list",l)
    

add()
