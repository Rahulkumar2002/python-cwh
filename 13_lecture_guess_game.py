import random

randomNo = random.randint(1, 100)
guessNo = 0
while True:
    userGuess = int(input("Enter your guess:"))
    if(userGuess == randomNo):
        print(f"You guess is correct : {randomNo}")
        break
    elif(userGuess < randomNo):
        print("You guessd low , guess higher.")
    elif(userGuess > randomNo):
        print("You guessd high , guess somewhat low.")
    guessNo = guessNo + 1

print(f"No of guess it took to reach to correct ans is {guessNo + 1}.")
