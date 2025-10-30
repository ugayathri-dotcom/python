def fun1():
    d={}
    n=int(input("Enter no of elements"))
    for i in range(n):
        key=input("Enter key")
        val=input("Enter value")
        d[key]=val
    
    print("Created dictionary",d)

    d.popitem()
    print("after removing key",d)
        
fun1()
    
