#Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/_
_____/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = str(input('you\' want to go "left" or "right" ? type left or right ')).lower()
if choice1 == "left" :
    choice2 = input('you\' came to the lake.there is an island in the middle of the lake type "wait" to wait for the boat type "swim" to swin across. ')
    if choice2 == "wait":
       choice3 = input("you arrive at island unharmed.there is a house with 3 doors.one red,one blue and one blue.which color do you want to choose. ")
       if choice3 == "red":
            print("it is room full of fire. game over")
       elif choice3 == "yellow":
            print("you found the trasure. YOU WON!!!")
       elif choice3 == "blue":
            print("you enter in room of beasts.GAME OVER")
       else:
            print("you choose the door that doesn't exist")

    else:
        print("you got attacked by angry trout. game over")    
else: 
    print("you fell into a hole.Game Over")   
