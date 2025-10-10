n=int(input("Enter no"))
if n <= 0:
    print("Invalid No")
else:
    i=1
    fact=1
    while(i<=n):
        fact = fact*i
        i+=1
print("The Factorial of given no",fact)
        
