from LearnPythonBasics.OOPS.inheritance.learn_inheritance import Calculate

class Calc(Calculate):
    def __init__(self):
        Calculate.__init__(self,120,50)
    def subtact(self):
        return self.x-self.y

subtract=Calc()
print(subtract.subtact())