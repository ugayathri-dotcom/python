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
s3=s.intersection(s1)
print("Intersection value",s3)
s2=s.symmetric_difference(s1)
'''d=s-s3   #both methods can be used
d1=s1-s3
s2=d.union(d1)'''
print("After removing intersectional values",s2)
    
