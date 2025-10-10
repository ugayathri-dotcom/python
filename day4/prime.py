a=int(input("Enter no"))
count=0
if a == 1:
    print("1 is Not a Prime no")
else:
        for i in range (2,a):
            if a % i == 0:
                count+=1


if count == 0:
    print("The given no is Prime")
    

else:
    print("The given no is Not Prime")
        
        
