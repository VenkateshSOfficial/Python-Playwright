class Calculate:
    num=100 # ==> class variables
    ## below is the syntax to create constructor in Python
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("I am constructor")

    def add(self):
        return self.x+self.y + Calculate.num

cal=Calculate(2,3) ## ===> object creation syntax
print(cal.add())

cal1=Calculate(10,20)
print(cal1.add())