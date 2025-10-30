def create():
    l=[]
    s=0
    n=int(input("Enter no of elements"))
    for i in range (n):
        val=int(input("enter value"))
        l.append(val)
        s+=val
    print("Created list",l)
    return l
s1=0
create()
s1=sum(l)
print(s1)


'''s=0
create()
s=sum+5
print(s)'''
