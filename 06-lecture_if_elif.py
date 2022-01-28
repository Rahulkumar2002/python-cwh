# if and elif ladder
# a = 45
# if(a < 3):
#     print("a is greater than 3")
# elif(a > 15):
#     print("a is greater than 15")
# else:
#     print("a is less than 45")

# When there is only if statements :
# a = 9
# if(a > 3):
#     print("Greater than 3")

# if(a > 4):
#     print("Greater than 4")

# if(a > 9):
#     print("Greater than 9")
# else:
#     print("Not greater than 9")


# # Write a program to print yes for age greater than or equal to 18 :
# age = int(input("Enter your age : "))
# if(age >= 18):
#     print("Yes")
# else:
#     print("No")

# Practice set :
# Write a program to print greatest of 4 number inputed by user :
# num1 = int(input("Enter number : "))
# num2 = int(input("Enter number : "))
# num3 = int(input("Enter number : "))
# num4 = int(input("Enter number : "))

# if(num1 > num2):
#     if(num1 > num3):
#         if(num1 > num4):
#             print(num1, " is greates of all 4")
#         elif(num4 > num1):
#             print(num4, " is greates of 4")
#     elif(num3 > num1):
#         if(num3 > num4):
#             print(num3, " is greates of all 4")
#         elif(num4 > num3):
#             print(num4, " is greates of 4")
# elif(num2 > num1):
#     if(num2 > num3):
#         if(num2 > num4):
#             print(num2, " is greates of all 4")
#         elif(num4 > num2):
#             print(num4, " is greates of 4")
#     elif(num3 > num2):
#         if(num3 > num4):
#             print(num3, " is greates of all 4")
#         elif(num4 > num3):
#             print(num4, " is greates of 4")
# Write a program to check if a student is passed or failed if each subject require 33% to pass and total of 40% to pass :

# maths = int(input("Enter marks of Math : "))
# science = int(input("Enter marks of Science : "))
# sst = int(input("Enter marks of SST : "))
# total = (maths + science + sst)/3

# if(maths >= 33):
#     print("Passed in Maths")
# else:
#     print("Failed in Maths")
# if(science >= 33):
#     print("Passed in Science")
# else:
#     print("Failed in Science")
# if(sst >= 33):
#     print("Passed in SST")
# else:
#     print("Failed in SST")
# if(total >= 40):
#     print("Passed total marks is greate than 40%")
# else:
#     print("Failed total marks is less than 40%")

# # Write a program to check if the given username contains less than 10 character :
# username = input("Enter your username : ")
# lenght = len(username)

# if(lenght < 10):
#     print("Username contains less than 10 characters.")
# else:
#     print("Username contains more than or equal to 10 characters.")

# # # Write a program to check for a give no. in the list :

# a = [20, 2, 1, 3, 4, 5, 6, 7, 8]
# num = int(input("Enter the number you want to find : "))
# print(num in a)

# Write  a program to find grades of the given number from the followind schema :
# 90-100 : Ex
# 80-90 : A
# 70-80 : B
# 60-70 : C
# 50-60 : D
# 40-50 : E
# 30-40 : F

# marks = int(input("Enter your marks to get the grades : "))

# if(marks < 100 and marks >= 90):
#     print("Grades : Ex")
# elif(marks < 90 and marks >= 80):
#     print("Grades : A")
# elif(marks < 80 and marks >= 70):
#     print("Grades : B")
# elif(marks >= 60 and marks < 70):
#     print("Grades : C")
# elif(marks < 60 and marks >= 50):
#     print("Grades : D")
# elif(marks < 50 and marks >= 40):
#     print("Grades : E")
# else:
#     print("Grades : F")

# WAP to detect that post is talking about Harry :

# post = input("Enter your post : ")

# if("Harry" in post):
#     count = True
# elif("harry" in post):
#     count = True
# elif("hARRY" in post):
#     count = True
# elif("HaRRy" in post):
#     count = True
# else:
#     count = False

# if(count):
#     print("Your post is talking about Harry")
# else:
#     print("Your post is not talking about Harry")
