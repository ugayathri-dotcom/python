from datetime import datetime as d
class person:
    def __init__(self,name,country,birth_year):
        self.name=name
        self.country=country
        self.dob=birth_year

    def age(self):
        c=d.now().year
        age=c-self.dob
        print("Current age of",self.name,"is:",age)
        
name=input("Enter your name")
c=input("Enter country")
b=int(input("Enter birth year"))
p=person(name,c,b)
p.age()



        
