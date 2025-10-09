q=int(input("Enter the Cost of Purchased Quantity"))

if q > 1000:
    a=q*(10/100)
    c=q-a
    print("Discounted Price", c)

else: print("Not Eligible for Discount")
