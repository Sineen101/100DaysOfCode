print("````````````````Welcome To Treasure Island!```````````````````")

# raw string:
print(r'''********************************************************* 
      
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             \   _/ \_     <_o#\__/#o_>     _/ \_   /
                    \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.===||=== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
        *********************************************************
''')
side = input("You are at crossroads! Do you wanna go left or right?\n").lower()
if side == "left" or side == "l":
    action = input(
        "You reached a river. Do you wanna swim or wait for the boat?\n").lower()
    if action == "wait" or action == "w":
        print("You are at the boat. You are safe.\n")
        door = input(
            "You reached the other side of the river. Which door do you wanna open? Blue or Red or Yellow\n").lower()
        if door == "blue" or door == "b" or door == "red" or door == "r":
            print("Wrong pick! Game Over!")
        elif door == "yellow" or door == "y":
            print("You found the Treasure!")
        else:
            ("Wrong pick! Game Over!")
    else:
        print("Oops! An aligator got you! Game Over!")
else:
    print("You chose the wrong side! Game Over!")
