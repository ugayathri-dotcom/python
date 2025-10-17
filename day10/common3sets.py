s=set()
n=int(input("enter the no of elements"))
for i in range (n):
    val=input("Enter the value")
    s.add(val)
print("Created set1 is:",s)
s1=set()
n1=int(input("enter the no of elements"))
for j in range (n1):
    val1=input("Enter the value")
    s1.add(val1)
print("Created set2 is:",s1)
s2=set()
n2=int(input("enter the no of elements"))
for k in range (n2):
    val2=input("Enter the value")
    s2.add(val2)
print("Created set3 is:",s2)
s3=s.intersection(s1)
s4=s3.intersection(s2)
#print(s4)
if len(s4)>0:
    print("Two lists has atleast one value in common",s4) 
