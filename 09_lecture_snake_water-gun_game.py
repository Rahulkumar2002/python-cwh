import random


def gameWin(comp, you):
    if(comp == you):
        return None
    elif(you == "s"):
        if(comp == "w"):
            return True
        elif(comp == "g"):
            return False
    elif(you == "g"):
        if(comp == "s"):
            return True
        elif(comp == "w"):
            return False
    elif(you == "w"):
        if(comp == "g"):
            return True
        elif(comp == "s"):
            return False


def compTurn(randNo):
    if(randNo == 1):
        comp = "s"
    elif(randNo == 2):
        comp = "w"
    elif(randNo == 3):
        comp = "g"
    return(comp)


print("Computer's Turn to choose from Snake(s) Water(w) & Gun(g)")

randNo = random.randint(1, 3)
comp = compTurn(randNo)

you = input("Your's turn to choose from Snake(s) Water(w) & Gun(g) : ")

result = gameWin(comp, you)

print(f"You choose {you}")
print(f"Computer choose {comp}")

if(result):
    print("You won")
elif(result == False):
    print("Computer won")
elif(result == None):
    print("Game Tied")
