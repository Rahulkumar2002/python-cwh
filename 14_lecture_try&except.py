while True:
    print("input 'q' to quit the game.")
    a = input("Enter your no. :")

    try:
        if (a == 'q' or a == 'Q'):
            break
        a = int(a)
        if(a > 6):
            print("Your no. is greater then 6.")
        elif(a < 6):
            print("Your no. is less than 6.")
        elif(a == 6):
            print("Your no. is equal to six.")
    except Exception as e:
        # pass
        print(f"Your input created an error which is : {e}")

print("Thank you for playing this game.")
