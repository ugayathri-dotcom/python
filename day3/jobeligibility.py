a=int(input("Enter Aptitute Marks"))
if a >= 85:
    b=int(input("Enter GD Marks"))
    if b >= 90:
        c=int(input("Enter Technical Marks"))
        if c>= 80:
            d=int(input("Enter Marks in HR"))
            if d >= 95:
                print("Candidate Selected")
            else: print("Disqualified in HR round")
        else: print("Disqualified in Technical round")
    else: print("Disqualified in GD round")
else: print("Disqualified in Aptitude round")
    
