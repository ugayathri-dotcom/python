def add(**a):
    b=input("enter value")
    for key,val in a.items():
        if(val==b):
            print("given value found")
add(a=2,b=9,d=90)
