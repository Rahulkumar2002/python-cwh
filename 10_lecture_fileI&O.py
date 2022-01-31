# Used open() to read from a file .

# f = open("sample.txt", "r")
# data = f.read()
# # data = f.read(5) # Will read first 5 characters of the file .
# print(data)
# f.close()


# #Readline method will only read one line at a single call .

# f = open("sample.txt")
# # Will read first line .
# data = f.readline()
# print(data)

# # Will read second line .
# data = f.readline()
# print(data)

# # And so on ....

# f.close()

# #Modes of reading the file :
# #For writing in the file open with "w".
# #For reading in the file open with "r".
# #For appending in the file open with "a".
# #For updating in the file open with "+".
# #For reading in binary mode open file with "rb" .
# #For reading in text mode open file with "rt".

# To write in the file Note: if file is not present then it will be automatically created:

# f = open("writing.txt", "w")
# f.write("Please add this to the file .")
# f.close()

# f = open("writing.txt", "a")
# f.write("Append this to the file .")
# f.close()

# Best way to open a file is with "With" statement beacause it automatically closes the file .
# Note f.write() returns no. of character which are written at the current moment by the write function.

# with open("sample.txt", "a") as f:
#     data = f.write(
#         "This"
#     )

# print(data)


# PRACITCE SET :

# WAP to check wheter a file contains the word "twinkle" in it .

# with open("poem.txt", "r") as f:
#     data = f.read()

# if(("Twinkle" in data) | ("twinkle" in data)):
#     print("It contains twinkle.")
# else:
#     print("Donot contain.")

# WAP to check for highscore when ever it is brokend .

# def game():
#     return 50


# with open("history.txt", "r") as f:
#     data = f.read()

# currentHighScore = game()

# if (currentHighScore > int(data)):
#     print("Congratulations ! new high  score is created.")
#     with open("history.txt", "w") as f:
#         f.write(str(currentHighScore))

# elif(currentHighScore < int(data)):
#     print("You need to work hard.")

# elif(currentHighScore == int(data)):
#     print("High score is maintained.")


# # WAP to create a multiplication table of 2 - 20 and write it inside a file .

# for i in range(2, 21):
#     with open(f"tables/Multiplication_table_of_{i}.txt", "w") as f:
#         for j in range(1, 11):
#             f.write(f"{i} * {j} = {i * j} \n")

# # WAP to update "Donkey" with "########" in same file .

# with open("donkey.txt") as f:
#     data = f.read()
#     data = data.replace("donkey", "######")
# with open("donkey.txt", "w") as f:
#     f.write(data)
