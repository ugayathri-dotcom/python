y=int(input("Enter the year"))
s=int(input("Enter the semester"))

if y == 1 and s <= 2:
    print("Five Subjects:\n1.English \n2.Chemistry \n3.Physics \n4.Maths \n5.Fundamentals of Computer")

elif y == 2 and s <= 4:
    print("Five Subjects:\n1.OOPS \n2.DSP \n3.Data Structure \n4.DPSP \n5.Computer Programming")
elif y ==3 and s <= 6:
    print("Five Subjects: \n1.Advanced Data Structure \n2.Compiler Design \n3.Operating system \n4.Maths \n5.DBMS")
else:
    print("Invalid Year and Semester")
    
