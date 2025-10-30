def armstrong(n):
    #num=int(input("Enter a number"))
    sum=0
    t=n
    n1=len(str(n))
#print(n)
    while t>0:
        digit=t%10
        sum+=digit**n1
        t//=10
    if n==sum:
         print("It is an Armstrong no:",sum)
    else: print("It's not an Armstrong no")


    
