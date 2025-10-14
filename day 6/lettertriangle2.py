ch=65
a=int(input("Enter Rows"))
for i in range(1,a+1):

    for j in range(1,i+1):
        print(chr(ch),end=" ")
        
    print()
    ch+=1
