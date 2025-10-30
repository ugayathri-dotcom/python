def getvalue():
    d={}
    s=1
    n=int(input("Enter no of elements"))
    for i in range(n):
        key=int(input("Enter key"))
        val=int(input("Enter value"))
        d[key]=val
    print("created dictionary",d)
    k=int(input("Enter the key to get value"))
    print(d.get(k))
    print(d.values())
