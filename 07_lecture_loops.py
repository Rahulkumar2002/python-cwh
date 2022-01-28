# # WAP to print no. from 1 to 50 via a while loop :

# i = 1

# while (i <= 50):
#     print(i)
#     i += 1

# print("Done")

# # WAP to print content of a list via loops :

# i = 0
# arr = [10, 20, 30, 40, 50, 60]

# while (i < len(arr)):
#     print(arr[i])
#     i += 1

# for items in arr:
#     print(items)

# # Range function in for loop :

# for i in range(8):
#     print(i)

# # for loop with else :

# for i in range(10):
#     print(i)
# else:
#     print("Loop is over.")

# # Break statement in loops :
# # Note : else statements in loop will only execute when loop is stopped at completing its task not because of a
# # break statement .

# for i in range(10):
#     print(i)
#     if(i == 5):
#         break
# else:  # Inside this loop else statement won't be executed .
#     print("Your loop is successfully completed.")

# Continue statement in loops :
# Continue donot execute whatever is below it when used .

# for i in range(10):
#     if i == 5:  # It will skip the print(i) statement for i = 5 .
#         continue
#     print(i)

# Pass statement in loops :
# Pass is a null statement in python and when we use pass it means "Do Nothing" .

# i = 0
# if i > 4 :
#     pass
#
# print(45)

# PRACTICE SET :

# # Write a program to print multiplication table of a given number :
# n = int(input("Enter the no. : "))
# for i in range(1, 11):
#     print(n, " * ", i, " = ", n * i)

# i = 1
# n = int(input("Enter the no. : "))
# while i <= 10:
#     print(n, " * ", i, " = ", n * i)
#     i += 1

# # WAP to greet all names of the persons stored in the list l1 which starts with letter S :
# l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

# for item in l1:
#     if (item[0] == "S"):
#         print("Hello ,", item)
#     else:
#         continue

# for name in li:
#     if name.startswith("S"):
#         print("Hello" + name)


# # WAP to find wheter a given no. is prime or not :
# n = int(input("Enter your no. to check for prime no. : "))

# if(n == 2):
#     print("2 is a prime no.")
# else:
#     for i in range(2, n):
#         if (n % i == 0):
#             print(n, " is not prime")
#             break
#         elif (i == n-1):
#             print(n, " is a prime no.")
#             break
#         else:
#             continue

# # WAP to find sum of first n natural no. using while loops :

# n = int(input("Enter your no. : "))
# sum = 0
# for i in range(1, n+1):
#     sum += i

# print(sum)

# # WAP to find factorial using for loop :
# n = int(input("Enter your no. : "))
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

# WAP to print this pattern :
#     *
#   * * *
# * * * * *

# n = 3
# for i in range(3):
#     print(" " * (n-i-1), end="")
#     print("*" * (2*i+1), end="")
#     print(" " * (n-i-1))


# WAP to print this patten :
# *
# **
# ***

# for i in range(4):
#     print("*" * (i+1))
