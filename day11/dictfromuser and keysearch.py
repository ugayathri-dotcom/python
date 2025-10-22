d={}
n=int(input("Enter no of elements"))
for i in range(n):
    key=input("Enter key")
    val=input("Enter value")
    d[key]=val
    
print("Created dictionary",d)
count=0
d1=d.keys()
print("Keys",d1)
a=input("Enter key to search")
for j in d1:
    if j == a:
        count+=1      
    else:
        pass
       
if count!=0:
     print("Given key present in dictionary")
else:
    print("Given key not present in dictionary")
     
