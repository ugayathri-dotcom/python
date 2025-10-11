a=int(input("Enter Rows"))
ch=65

for i in range(0,a):
    for j in range(0,i+1):
        print(chr(ch+j),end=" ")
        #ch+=1

    print()
