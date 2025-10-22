d={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=input("Enter value")
    d[key]=val
    
print("Created dictionary",d)
print(type(d.items()))

for key,val in d.items():
    print(type(d.items()))
    '''print(key,val)
    print("Type of key",type(key))
    print("type of value",type(val))'''
