class BasicCalculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2

calc=BasicCalculator(10,5)
print("Addition:",calc.num1, "+",calc.num2,"=",calc.addition())
print("Subtraction:",calc.num1, "-",calc.num2,"=",calc.subtraction())
print("Multiplication:",calc.num1, "*",calc.num2,"=",calc.multiplication())
print("Division:",calc.num1, "/",calc.num2,"=",calc.division())