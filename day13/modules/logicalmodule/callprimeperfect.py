import prime as p,armstrong as a,perfect as pr

choice=int(input("enter your choice to check:\n1.To find Prime \n2.To find Armstrong,\n3.to find Perfect")) 
n=int(input("enter number"))
if choice==1:
    ans=p.prime(n)
    print(ans)
elif choice==2:
    ans=a.armstrong(n)
    print(ans)
elif choice==3:
    ans=pr.perfect(n)
    print(ans)
else: print("enter a valid choice")
