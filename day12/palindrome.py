def palindrome():
    a=input("enter a string")
    b=a[::-1]
    print("Reversed string",b)
    if a==b:
        print("The given string is a palindrome")
    else: print("The given string is not a palindrome")

palindrome()
