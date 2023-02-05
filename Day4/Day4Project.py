#ROCK PAPER SCISSORS GAME

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]

user_choice = int(input("what do you choose? Type 0 for rock, 1 for paper or 2 for Scissors "))

if user_choice >=3 or user_choice <0:
    print("you typed an invalid number you loose")
else:    
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)

    print("Computer choose: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Winss!!")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose")    
    elif computer_choice > user_choice:
        print("You loose")
    elif user_choice > computer_choice:
        print("YOU WIN!!")    
    elif computer_choice == user_choice:
        print("it's Draw")    


