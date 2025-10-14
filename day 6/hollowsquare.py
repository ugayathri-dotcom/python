a=int(input("Enter Grid pattern limit"))
for i in range (1,a+1):
    for j in range (1,a+1):
        if j==1 or i==1 or j==a or i==a:
           print("*",end="")
        else: print(" ",end="")
    print()
