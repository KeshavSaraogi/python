print("Welcome To Treasure Island!")
direction = input("Press l or r to chose a direction: ")

if direction == "r":
    print("Game Over")
elif direction == "l":
    action = input("Swim or Wait? ")
    if action == "swim":
        print("Game Over")
    elif action == "wait":
        door = input("Red/Blue/Yellow Which Door? ")
        if door == "yellow":
            print("You Win")
        elif door == "red" or door == "blue":
            print("Game Over")
        else:
            print("Invalid Door")
    else:
        print("Invalid Action")
else:
    print("Invalid Direction")