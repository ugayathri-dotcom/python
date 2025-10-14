a=int(input("Enter Row value"))
for i in range(a,0,-1):
    for j in range(1,i+1):
        if (i==a or j == 1 or j == i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

