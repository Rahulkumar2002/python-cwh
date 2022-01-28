# # myDict = {
# # "Fast" : "Hello I'm Fast" ,
# # "Name" : "Rahul",
# # "LastName":"Jha",
# # "LastName" :"Kumar"
# # } 
# # print(myDict)
# # print(myDict["Fast"]) #Printing value using key value pairs .
# # myDist["Fast"] = "Not so fast" #Dictionary is  Mutable .
# # print(myDict)
# # print(myDict["LastName"])#Overriding first key value pair of "LastName":"Jha" .


# # Methods of Dictinary : 

# # myDict = {
# #     "fast" : "Not so fast",
# #     "rahul": "a coder",
# #     "marks":[ 1 ,2 ,3 ],
# #     "anotherDict" : {'rahul':'player'},
# #     1 : 2
# # } 

# # print(list(myDict.keys())) #Prints keys of the myDict in the form of the list .
# # print(myDict.values()) #Prints value of the myDict in the form of the list .
# # print(myDict.items()) #Prints the (key , value ) for all contents of the dictionary .
# # print(myDict)
# # updateDict = {
# #     "fastlane":"a book",
# #     "name":"rahul"
# # }

# # myDict.update(updateDict)#Update the dictionary by adding key-values pairs from updateDict .
# # print(myDict)

# # print(myDict["anotherDict"]["rahul"])

# # print(myDict.get("rahul")) # Print value of the key "rahul"
# # print(myDict["rahul"]) # Print value of the key "rahul" 

# # print(myDict.get("rahul2")) # Return None because myDict do not containe a key "rahul2". 
# # print(myDict["rahul2"]) # Throw an error because "rahul2" is not present in the myDict .

# # #--------------------------------------Sets------------------------------------------
# # #Set is a collection of a non repetetive elements .

# # # Important : This syntax will create an empty Dictionary : 
# # a = {}
# # print(type(a))

# # # To create a empty set : 
# # b = set()
# # print(type(b))

# # # Methods of sets : 

# # # To add into sets : 
# # # Adding a value repeteadly cannot change the sets.
# # b.add(4)
# # b.add(5)
# # b.add(5)# Will not be added inside set because it is repeating . 

# # print(b) #{4 ,5}

# # # List can't be added inside Sets but Tuples can because value of List can be changed. 

# # # b.add([2 ,3 ,4]) #List (when try to add will throw an error)
# # # b.add({"Fast":"Fastlane"}) # Dictonary cannot be added to Sets .
# # b.add((1 , 3 ,4)) #Tuple
# # print(b)

# # #To get the length of the sets : 
# # print(len(b)) 

# # #To remove a element from the sets : 
# # # b.remove(5) # Removes 5 from sets b .
# # # b.remove(15) # Will throw error when try to remove 15 because 15 is not present in the set b .

# # # print(b)

# #Practice Set : 

# # # Write a program to help user find words in dictonary : 
# # myDict = {
# #     "Pankha":"Fan",
# #     "Vastu" : "Item",
# #     "Kela":"Banana"
# # } 
# # print(list(myDict.keys())) 
# # a = input("Choose from above keys : ")
# # print(myDict.get(a))

# # Write a program to get 8 no input from user and display all unique numbers : 

# egg1 = int(input("Enter your no. : "))
# egg2 = int(input("Enter your no. : "))
# egg3 = int(input("Enter your no. : "))
# egg4 = int(input("Enter your no. : "))
# egg5 = int(input("Enter your no. : "))
# egg6 = int(input("Enter your no. : "))
# egg7 = int(input("Enter your no. : "))
# egg8 = int(input("Enter your no. : "))

# s = {egg1 , egg2 , egg3 , egg4 ,egg5 , egg6 , egg7 , egg8}

# print(s)

# # Set with 18(int) and 18(str) ? 
# s = {18 , "18"}
# print(s)

# # Length of Set with 20  , 20.0 , "20" as element ? 

# s = {20 , 20.0 , "20"}
# print(len(s))
# print(s)

# Empty Dictionary and keys as name and value as their favourite language : 
Name1  = input("Rakesh enter your favourite lang : ")
Name2  = input("Ankit enter your favourite lang : ")
Name3  = input("Rohan enter your favourite lang : ")
Name4  = input("Rahul enter your favourite lang : ")

myDict = {
    "Rakesh":Name1 ,
    "Ankit" : Name2,
    "Rohan":Name3,
    "Rahul":Name4
}

print(myDict)