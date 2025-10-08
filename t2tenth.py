name=input("Enter your Name:")
r=int(input("Enter your Rollno:"))
t=int(input("Enter Tamil Mark:"))
e=int(input("Enter English Mark:"))
m=int(input("Enter Maths Mark:"))
s=int(input("Enter Science Mark:"))
ss=int(input("Enter Social Science Mark:"))
sum=t+e+m+s+ss
per=(sum/500)*100
print(f"Name:{name}\nRollno:{r} \nTamil:{t} \nEnglish:{e} \nMaths:{m} \nScience:{s} \nSocial Science:{ss} \nTotal:{sum} \nPercentage:{per}")


