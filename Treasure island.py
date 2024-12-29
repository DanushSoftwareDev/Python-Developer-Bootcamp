print("""
                          +........+
                          J||||||||L
                         |           |
                       ~|~~~~~~~~~~~~|~
                       |              |
                    ~~|~~~~~~~~~~~~~~~~|~~
        _--^I^--_    |                  |
       / /^~|~^\ \~~~~~~+~+~~~~~~~~+~+~~~~~
      / /   |   \ \     | |        | |
      | |   |   | |     = =        = =
~~~~~~~ |   |o  | ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
------- |   |   | ---------------------------------
------- |   |   | ---------------------------------
======= |===|===| ================================

       
""")
print("_________________________________________________________________________________________________________________")
print("Welcome to Treasure Island.\nYour mission is to find the treasure")
step1=input("You're at a cross road. Where do you want to go?\n\t type 'left' or 'right'\n")
if step1 == "left":
    step2=input("You've come to a lake. There is an island in the middle of the lake\n Type 'wait' to wait for a boat. Type 'swim' to swim across\n")
    if step2 == "wait":
        step3=input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow, and one blue. Which colour do you choose.\n")
        if step3 == "yellow":
            print("You found the treasure! You Win!")
        elif step3 == "red":
            print("Ahhh! Burned by fire. GAME OVER")
        elif step3 == "blue":
            print("NOOO!!! HEEEELPPPPPpppp!!!!! Eaten by beasts. Game Over.")
        else:
            print("GAME OVER. Better luck next time.")
    else:
        print("you were attacked by trouts. GAME OVER")
else:
    print("You fell into a hole game over!!!")


