def perfect(n):
    #a=int(input("Enter a value"))
    sum=0
    for i in range(1,n):
            if n%i==0:
                sum+=i
    if sum == n:
            print("the given no is perfect")
    else :  print("the given no is not perfect")


