y=int(input("Enter the year"))
s=int(input("Enter the semester"))

if y == 1 and s == 1:
    print("Five Subjects:\n1.English \n2.Chemistry \n3.Physics \n4.Maths \n5.Fundamentals of Computer")
elif y==1 and s == 2:
    print("Five Subjects:\n1.Environmental Science \n2.Engineering Drawing \n3.Applied Physics \n4.Maths \n5.Calculus")
elif y == 2 and s == 3:
    print("Five Subjects:\n1.OOPS \n2.DSP \n3.Data Structure \n4.DPSP \n5.Computer Programming")
elif y == 2 and s == 4:
    print("Five Subjects:\n1.Mechanics of fluids \n2.Thermo dynamics \n3.Control system \n4.Material Science \n5.Theory of computation")    
elif y == 3 and s == 5:
    print("Five Subjects: \n1.Advanced Data Structure \n2.Compiler Design \n3.Operating system \n4.Maths \n5.DBMS")
elif y == 3  and s == 6:
    print("Five Subjects: \n1.Artificial Intelligence \n2.Advanced Compiler Design \n3.Operating system \n4.Cyber security \n5.CCNA")
elif y == 4 and s == 7:
    print("Five Subjects: \n1.Project work \n2.Big Data \n3.Professional Ethics \n4.Human Values \n5.DataBase")
elif y == 4 and s == 8:
     print("Five Subjects: \n1.Frame Work \n2.Algorithms \n3.Discrete Mathematics \n4.Digital Logic Design \n5.EG")
else:
    print("Invalid Year and Semester")
    
