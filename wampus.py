wumpus = [["Save", "Breeze", "PIT", "Breeze"],
          ["Smell", "Save", "Breeze", "Save"],
          ["WUMPUS", "GOLD", "PIT", "Breeze"],
          ["Smell", "Save", "Breeze", "PIT"]]

row = 0
column = 0
arrow = True
player = True
score = 0

while(player):
    choice = input("Press u to move up\nPress d to move down\nPress l to move left\nPress r to move right\n")

    if choice == "u":
        if row != 0:
            row -= 1
        else:
            print("Move denied")

        print("Current location:", wumpus[row][column], "\n")

    elif choice == "d":
        if row != 3:
            row += 1
        else:
            print("Move denied")

        print("Current location:", wumpus[row][column], "\n")

    elif choice == "l":
        if column != 0:
            column -= 1
        else:
            print("Move denied")

        print("Current location:", wumpus[row][column], "\n")

    elif choice == "r":
        if column != 3:
            column += 1
        else:
            print("Move denied")

        print("Current location:", wumpus[row][column], "\n")

    else:
        print("Move denied")

    if wumpus[row][column] == "Smell" and arrow != False:
        arrow_choice = input("Do you want to throw an arrow? -->\nPress y to throw \nPress n to save your arrow\n")

        if arrow_choice == "y":
            arrow_throw = input("Press u to throw up\nPress d to throw down\nPress l to throw left\nPress r to throw right\n")

            if arrow_throw == "u":
                if wumpus[row-1][column] == "WUMPUS":
                    print("Wumpus killed")
                    score += 1000
                    print("Score:", score)
                    wumpus[row-1][column] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted")
                    score -= 10
                    print("Score:", score)

            elif arrow_throw == "d":
                if wumpus[row+1][column] == "WUMPUS":
                    print("Wumpus killed")
                    score += 1000
                    print("Score:", score)
                    wumpus[row+1][column] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted")
                    score -= 10
                    print("Score:", score)

            elif arrow_throw == "l":
                if wumpus[row][column-1] == "WUMPUS":
                    print("Wumpus killed")
                    score += 1000
                    print("Score:", score)
                    wumpus[row][column-1] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted")
                    score -= 10
                    print("Score:", score)

            elif arrow_throw == "r":
                if wumpus[row][column+1] == "WUMPUS":
                    print("Wumpus killed")
                    score += 1000
                    print("Score:", score)
                    wumpus[row][column+1] = "Save"
                    wumpus[1][0] = "Save"
                    wumpus[3][0] = "Save"
                else:
                    print("Arrow wasted")
                    score -= 10
                    print("Score:", score)

            arrow = False

    if wumpus[row][column] == "WUMPUS":
        score -= 1000
        print("\nWumpus here!!\nYou die\nAnd your score is:", score, "\n")
        break

    if wumpus[row][column] == "GOLD":
        score += 1000
        print("GOLD FOUND! You won....\nYour score is:", score, "\n")
        break

    if wumpus[row][column] == "PIT":
        score -= 1000
        print("\nAhhhh!!!!\nYou fell in the pit\nAnd your score is:", score, "\n")
        break
