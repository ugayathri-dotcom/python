def prime(*l1):
    l=list()
    l1=list()

    n=int(input("Enter no of elements"))
    for i in range(n):
        val=int(input("Enter the elements"))
        l.append(val)
    
    print("created list is",tuple(l))

    for j in l:
        if j>1:
            sum=0
            for k in range(1,j):
                if j%k==0:
                    sum+=k
            if sum == j:
                l1.append(j)
    
    print("The perfect no's",tuple(l1))

prime()
    
