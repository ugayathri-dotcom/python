name=input("Enter your Name:")
r=int(input("Enter your Rollno:"))
t=int(input("Enter Tamil Mark:"))
e=int(input("Enter English Mark:"))
m=int(input("Enter Maths Mark:"))
p=int(input("Enter Physics Mark:"))
c=int(input("Enter Chemistry Mark:"))
b=int(input("Enter Biology Mark:"))

sum=t+e+m+p+c+b
per=(sum/1200)*100
print(f"Name:{name}\nRollno:{r} \nTamil:{t} \nEnglish:{e} \nMaths:{m} \nPhysics:{p} \nChemistry:{c} \nBiology:{b} \nTotal:{sum} \nPercentage:{per}")


