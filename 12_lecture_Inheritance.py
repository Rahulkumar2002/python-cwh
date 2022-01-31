# Single level inheritance(One parent one child).

#    Parent
#      |
#      -> Child

# class Employee:
#     company = "Google"

#     def showDetails(self):
#         print("This is an employee.")


# class Programmer(Employee):
#     # company = "Yotube"
#     language = "Python"

#     def showLang(self):
#         print(f"Your language is {self.language}.")

#     # def showDetails(self):
#     #     print("This is an programmer.")


# e = Employee()
# p = Programmer()

# print(e.company)
# e.showDetails()
# print(p.company)
# p.showDetails()
# p.showLang()

# # Multiple inheritance (More than one parent but only one child):

#  Parent1             Parent2
#    |                     |
#    ->        Child      <-

# class Employee:
#     company = "Visa"


# class Freelancer:
#     company = "Fiverr"


# class Programmer(Employee, Freelancer):
#     name = "Rohit"


# p = Programmer()
# print(p.company)
# print(p.name)

# Multilevel Inheritance (One parent one child but child will become parent for next child):

#            Parent
#              |
#            Child1
#              |
#            Child2

# class Person:
#     country = "India"

#     def takeBreak():
#         print('I am breathing.')


# class Employee(Person):
#     company = "Honda"
#     salary = 100

#     def getSalary(self):
#         print(f"Your salary is {self.salary}.")


# class Programmer(Employee):
#     company = "Fiver"

#     def getSalary(self):
#         print("Programmer don't get salary.")


# p = Programmer()
# e = Employee()
# pr = Person()

# print(p.company)
# p.getSalary()
# e.getSalary()
# print(pr.country)


# # Class Methods :

# from pkg_resources import safe_extra


# class Employee:
#     salary = 100
#     company = "camel"
#     location = "Delhi"

#     # def changeSalary(self, sal):
#     #     self.__class__.salary = sal

#     # Class Method is used to modify our function to be able to change class attributes .
#     @classmethod
#     def changeSalary(cls, sal):
#         cls.salary = sal


# e = Employee()
# print(e.salary)
# e.changeSalary(455)
# print(e.salary)

# PRACTISE SET :

# # WAP to create a 2d vector class a make a 3d vectore class from it .

# from textwrap import TextWrapper


# class twoDVector:
#     x = 0
#     y = 0
#     z = 0

#     def createVector(self):
#         print(f"Vector is : {self.x}i + {self.y}j + {self.z}k")


# class threeDVector(twoDVector):
#     x = 0
#     y = 0
#     z = 0

#     # def createVector(self):
#     #     print(f"Vector is : {self.x}i + {self.y}j + {self.z}k")


# vec = twoDVector()
# vector = threeDVector()
# vec.x = 10
# vec.y = 10
# vector.x = 20
# vector.y = 20
# vector.z = 20
# vec.createVector()
# vector.createVector()

# # WAP to create a class pet from class animal after than create a class dog from the pet class and add a method bark to it .

# class Animal:
#     legs = 4
#     ears = 2
#     type = "carnivorus"
#     residence = "Forest"


# class Pet(Animal):
#     residence = "House"
#     type = "Omnivorus or Herbivorus"


# class Dog(Pet):
#     residence = "Home"
#     type = "Omnivorus"

#     def bark(self):
#         print("Dogs can bark loud")


# dog = Dog()
# dog.bark()
# print(dog.residence)
# print(dog.legs)


# # WAP to implement complex no. and add __add__ and __mul__ to perform addition and multiplication on them.

# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#         print(f"{self.rea} + {self.img}i")

#     def __add__(self, comp):
#         return f"{self.real + comp.real} + {self.img + comp.img}i"

#     def __mul__(self, comp):
#         return f"{self.real * comp.real - self.img * comp.img} + {self.real * comp.img + self.img * comp.real}i"


# comp1 = complex(3, 2)
# comp2 = complex(1, 7)

# sum = comp1 + comp2
# mul = comp1 * comp2
# print(sum)
# print(mul)
