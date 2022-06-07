print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("WELCOME TO TREASURE ISLAND")
print("You are on mission to find treasure")
choice1 = input('You are on crossroad,where you want to go ? Type "left" or "Right".').lower()
if choice1 == left:
    input('You have come into the lake.There is an island in the middle of the lake.Type "wait" to wait for the boat or Type "Swim" toward islands').lower()
    if choice2 == wait:
        choice3 = input('You have three door "Yellow","Red","Blue",which color do you choose').lower()
        if choice3 == "Red":
            print("Room Full of Fire.Game Over")
        elif choice3 == "Yellow":
            print("Room full of Treasure.You Win")
        elif choice3 == "Blue":
            print("Room full of poisonous snake.Game Over")
        else:
            print("Wrong door.Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
