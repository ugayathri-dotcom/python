def facto(x):
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact

n=int(input("Enter n"))
r=int(input("Enter r"))
if r>n:
    print("Invalid")
else:
    ncr=facto(n)/((facto(r))*(facto(n-r)))
print("Combination ",ncr)
    
