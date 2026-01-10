from LearnPythonBasics.OOPS.constructor.learn_constructor import Calculate

class childImpl(Calculate):

    def multiply(self):
        return self.x*self.y+self.num

multiply=childImpl(12,15)
print("{} {}".format("The multiplication answer is : " , multiply.multiply()))