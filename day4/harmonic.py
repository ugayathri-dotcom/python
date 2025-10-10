n=int(input("Enter no"))
sum=0
if n<0:
    print("enter a Positive no")
else:
    for i in range (1,n+1):
        print(f"1/{i}")
        sum+=(1/i)
        """if i==n:
            print(" ")
        else:"""
           # print(f"1/{i}")
          
print("Sum of Harmonic Series ",sum)
        
