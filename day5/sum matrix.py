a=int(input("Enter Multiplication Grid pattern limit"))

sum=0
for i in range (1,a+1):
    for j in range (1,a+1):
        #s=j
        print(f"{j}",end=" ")
        sum+=j
    print()
print("The sum of elements of Matrix",sum)




       
       
