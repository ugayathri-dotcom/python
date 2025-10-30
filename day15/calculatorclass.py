class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(Self,x,y):
        return x/y

a=int(input("enter a"))
b=int(input("enter b"))
obj=calculator()
print("Addition",obj.add(a,b))
print("subtraction",obj.sub(a,b))
print("Multiplication",obj.mul(a,b))
print("division",obj.div(a,b))
