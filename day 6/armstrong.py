num=int(input("Enter a number"))
sum=0
t=num
n=len(str(num))
#print(n)
while t>0:
    digit=t%10
    sum+=digit**n
    t//=10
if num==sum:
     print("It is an Armstrong no:",sum)
else: print("It's not an Armstrong no")
