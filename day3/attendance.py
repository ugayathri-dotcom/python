a=int(input("Enter No of classes held"))
b=int(input("Enter No of class Attended"))
c = (b/a)*100
print("Percentage of class attended:", c)
if c > 75:
    print("Student allowed to sit in exam")
else: print("Student not allowed to sit in exam")
      
