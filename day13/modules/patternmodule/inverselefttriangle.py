def inverselefttriangle(a):
#a=int(input("Enter Inverse Left Triangle value"))
    for i in range(a,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()
