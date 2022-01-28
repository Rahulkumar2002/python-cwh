
# print(a)
# print(a[0:4])
# print(a[-4:])

# a = ["Rahul" , "Kumar" , "Jha"]
# # print("first Name = ",b[0])
# # print("middle Name = ",b[1])
# # print("last Name = ",b[2])
# a = [10 , 20 , 0 , True , False]
# a.sort()
# print(a)

#List methods : 

# a = [1 ,2 ,24 ,10 , 11 , 7 , 4 , 5] 

# print(a)
# a.sort() #Sort the list in ascending order.
# print(a)
# a.reverse() #Reverse the list .
# print(a)
# a.append(20)#Add 20 at the end of the list .
# print(a)
# a.insert(2 , 20000)#Add 20000 at index 2 of the list .
# print(a)
# a.pop(3)#Pop element at index 3 .
# print(a)
# a.remove(20000)#Remove 20000 from the list .
# print(a)

#-------------------Tuples--------------------------

#Declaring a Tuple : 
# t = (1 ,2 ,3 ,4 ,5) 
# t1 = ()#Empty Tuple
# t2 = (1 ,) #Single Element Tuple 
# print(t) #Printing a Tuple
# print(t1) #Printing a Empty Tuple
# print(t2) #Printing a Single Element Tuple
# print(t[0]) #Printing value at index 0 of a Tuple


# Methods in a Tuple : 
# Note : Values of a Tuple cannot be changed after declaration .

# t = (1 ,2 ,3 ,4 ,5 ,1 , 4 ,1) 

# print(t.count(1)) #Return no. of 1 present inside our Tuple t 
# print(t.count(4)) #Return no. of 1 present inside our Tuple t
# print(t.index(1)) #Return first index at which 1 is present 
# print(t.index(4)) #Return first index at which 4 is present 


#Practise Set : 

# # Program to store a list of seven fruits enterd by user : 
# a0 = input("Enter Name of First fruit : ")
# a1 = input("Enter Name of First second : ")
# a2 = input("Enter Name of First third : ")
# a3 = input("Enter Name of First four : ")
# a4 = input("Enter Name of First five : ")
# a5 = input("Enter Name of First six : ")
# a6 = input("Enter Name of First seven : ")

# a = [a0 , a1 , a2 , a3 , a4 , a5 , a6]  
# print(a) 

# #Write a program to accept marks of 6 student a dispaly them in a sorted manner 

# a0 = int(input("Enter Marks 1 : "))
# a1 = int(input("Enter Marks 2 : "))
# a2 = int(input("Enter Marks 3 : "))
# a3 = int(input("Enter Marks 4 : "))
# a4 = int(input("Enter Marks 5 : "))
# a5 = int(input("Enter Marks 6 : "))
# a6 = int(input("Enter Marks 7 : "))

# a = [a0 , a1 , a2 , a3 , a4 , a5 , a6]  
# a.sort()
# print(a) 

# #Write a program to check that tuple cannot be changed in python : 

# a =(1 , 2, 3, 4, 5) 

# a[0] = 2 #It will throw an error .

# print(a)

# # Write a program to sum a list with 4 numbers : 

# a = [ 1 , 2 ,3 ,4] 

# sum = a[0] + a[1] + a[2] + a[3] 

# print(sum) 

#Write a program to count no. of 0 in the followin tuple : 

# a = (7,0,8,0,0,9) 
# print(a.count(0))
