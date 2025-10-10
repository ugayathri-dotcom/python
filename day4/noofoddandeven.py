even =0
odd=0
a=int(input("enter no lower limit"))
b=int(input("enter no upperlimit"))
for i in range (a,b):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Total Odd no:",odd)
print("Total even no:",even)
