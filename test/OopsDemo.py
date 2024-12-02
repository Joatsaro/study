class Calculator:
    num = 100  # class variables (constants)

    # default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2, 3)  # syntax to create objects in python
obj.getData()
print(obj.num)
print(obj.Summation())

obj1 = Calculator(3, 4)  # syntax to create objects in python
obj1.getData()
print(obj1.num)
