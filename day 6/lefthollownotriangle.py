a=int(input("Enter Grid pattern limit"))
for i in range (1,a+1):
    for j in range (1,a+1):
        if j==1  or j==i or i==a:
           print(j,end=" ")
        else: print(" ",end=" ")
    print()
