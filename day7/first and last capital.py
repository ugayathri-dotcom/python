a=input("Enter a string")
if len(a)>=2 :
    b=a[0].upper()+a[1:-1]+a[-1].upper()
elif len(a)==1:
    b=a.upper()
else: b=a

print("After changing 1st and last letter to upper case:",b)

