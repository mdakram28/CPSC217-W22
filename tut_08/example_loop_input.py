power = 5

while power > 0:
    print("Available power : {0}".format(power))
    user_choice = input("Press enter to proceed or q to quit")
    if user_choice == "q":
        break
    power -= 1

print("Game Over")
