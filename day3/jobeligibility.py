a=int(input("Enter Aptitute Marks"))
if a >= 85:
    b=int(input("Enter GD Marks"))
    if b >= 90:
        c=int(input("Enter Technical Marks"))
        if c>= 80:
            d=int(input("Enter Marks in HR"))
            if d >= 95:
                print("Candidate Selected")
                t=a+b+c+d
                if t >390 and t <= 400:
                    print("Salary Eligibility is Rs.30000")
                elif t > 380 and t <=390:
                    print("Salary Eligibility is Rs.28000")
                elif t > 370 and t <= 380:
                    print("Salary Eligibility is Rs.25000")
                elif t > 350 and t <= 370:
                    print("Salary Eligibility is Rs.30000")
                    
            
                
            else: print("Disqualified in HR round")
        else: print("Disqualified in Technical round")
    else: print("Disqualified in GD round")
else: print("Disqualified in Aptitude round")


    
