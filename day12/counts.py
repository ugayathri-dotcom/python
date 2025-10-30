def count():
    a=input("Enter a sring")
    c=0
    b=0
    z=0
    for ch in a:
        if ch.lower() in ['a','e','i','o','u']:
           c=c+1
        elif ch.isalpha():
            b+=1
        elif not ch.isspace():
            z+=1
            
    print("No of vowels",c)
    print("no of consonants",b)
    print("No of special character",z)

count()
