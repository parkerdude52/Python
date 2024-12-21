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

#real code below this line 👇
game_images = [rock, paper, scissors]

import random
choice = int(input("What do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.\n"))
if choice >= 3 or choice < 0:
    print("you typed wrong! YOU LOSE! YOU LOSE!! YOU LOSE!!!")   
else:
    print(game_images[choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice])

    if choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and choice == 2:
        print("You win")
    elif computer_choice > choice:
        print("You lose")
    elif choice > computer_choice:
        print("You lose")
    elif computer_choice == choice:
        print("It's a draw")


