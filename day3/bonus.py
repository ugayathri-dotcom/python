s=int(input("Enter the Salary"))
y=int(input("Enter year of service"))
if y > 5:
    a=s*(5/100)
    s=a+s
    print("Net Bonus Amount",a)
    print("Salary after Bonus",s)
else: print("Not eligible for bonus")
