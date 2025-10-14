a=int(input("Enter Inverse Right Triangle"))
for i in range (a,0,-1):
    for j in range(0,a-i):
        print("",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
