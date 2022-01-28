# # WAP to find greatest of three no using functions :

# f = 0


# def greatest(a, b, c):
#     if(a > b):
#         if(a > c):
#             f = a
#         else:
#             f = c
#     else:
#         if(b > c):
#             f = b
#         else:
#             f = c
#     return f


# print(greatest(10, 40, 30))

# # WAP to find farenheight from celcius using functions :

# def far(x):
#     return (((9/5) * x) + 32)


# print(far(100))

# WAP to print python print function to not print "\n" at the end of the line .

# print("Hello", end="")
# print("Hello", end="")

# # WAP recursive function to find sum of the function :

# def sum(n):
#     if(n > 0):
#         add = n + sum(n-1)
#     else:
#         return 0
#     return add


# print(sum(10))

# # WAP to print this pattern :

# def pattern(n):
#     for i in range(n):
#         print("*" * (n - i), end="")
#         print(" " * (n - i))


# pattern(3)

# # WAP to convert inches in cms :

# def conv(x):
#     return x * 2.54


# print(conv(5))

# WAP to find multiplication of a number using functions and also a function to remove a element from a list:

# def mult(x):
#     for i in range(1, 11):
#         print(f"{x} * {i} = {x * i}")


# def destroy(abc, word):
#     abc.remove(word)


# a = ["hello", "here", "is", "Rahul", "Here"]
# # print(a)

# # mult(10)
# destroy(a, "here")
# destroy(a, "Rahul")
# print(a)
