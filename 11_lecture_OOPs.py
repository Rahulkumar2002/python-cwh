# class Employee:
#     company = "Google"


# harry = Employee()
# rahul = Employee()

# print(harry.company)
# print(rahul.company)

# Employee.company = "Youtube"

# print(harry.company)
# print(rahul.company)


# PRACTICE SET :
# # WAP to store information of programmers working at microsoft .

# class Programmer:
#     company = "Mcirosoft"

#     def __init__(self, name, product, id):
#         self.name = name
#         self.product = product
#         self.id = id

#     def getInfo(self):
#         print(
#             f"The name of programmer is {self.name} , it's id is {self.id} & product it has been working on is {self.product}.")


# rahul = Programmer('Rahul', 'Excel', '01')
# harry = Programmer('Harry', 'Skype', '02')

# rahul.getInfo()
# harry.getInfo()

# # WAP to work as a calculator which can perform square , cube & square roots of a number .

# class Calculator:
#     def __init__(self, operation, num):
#         self.operation = operation
#         self.num = num

#     def performCalc(self):
#         if (self.operation == "square"):
#             return (self.num)*(self.num)
#         elif (self.operation == "squareroot"):
#             return (self.num ** 0.5)
#         elif (self.operation == "cube"):
#             return (self.num)*(self.num)*(self.num)

#     @staticmethod
#     def greet():
#         print("Hello ")


# operation = input("Enter your operation as square , cube & squareroot : ")
# num = int(input("Enter your no. : "))
# calc = Calculator(operation, num)
# calc.greet()
# a = calc.performCalc()
# print(a)

# WAP
