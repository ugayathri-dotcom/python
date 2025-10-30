import sumofvalues as s,printvalues as p,getvaluesdict as get
wish=int(input("Enter no to wish\n1.To sum the values of dictionary.\n2.To print the values.\n3.Get values"))
if wish==1:
    s.sumdict()
elif wish==2:
    p.printvalues()
elif wish==3:
    get.getvalue()

