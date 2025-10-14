a=input("Enter a Word")
b=a[::-1]
if a == b:
    print(f"Entered Word is palidrome,{a} = {b}")
else:
    print("Its not a palindrome")
