print("Welcome to guess a number!\nI'm thinking of a number between 1 & 100")

import random
import os

def hard():
    """The hard version of the game"""
    end = False
    number = random.randint(1, 101)
    turns = 5
    print(f"The number is {number}")
    while not turns  == 0:
        guess1 = int(input("Make a Guess: "))
        if guess1 > number:
            print("Too High\n Guess Again.")
            turns -= 1
        elif guess1 == number:
            print("You Win")
            end = True
            turns == 0
            return
        else:
            print("Too Low.\nGuess Again.")
            turns -= 1


        guess2 = int(input("Make a Guess: "))
        if guess2 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess2 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess3 = int(input("Make a Guess: "))
        if guess3 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess3 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess4 = int(input("Make a Guess: "))
        if guess4 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess4 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1



        guess5 = int(input("Make a Guess: "))
        if guess5 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess5 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1
    else:
        os.system("cls")
        return
    
def easy():
    """The easy version of the game"""
    end = False
    turns = 10
    number = random.randint(1, 101)
    print(f"The number is {number}")
    while not turns == 0:
        guess1 = int(input("Make a Guess: "))
        if guess1 > number:
            print("Too High\n Guess Again.")
            turns -= 1
        elif guess1 == number:
            print("You Win")
            turns = 0
            end = True
            return
        else:
            print("Too Low.\nGuess Again.")
            turns -= 1


        guess2 = int(input("Make a Guess: "))
        if guess2 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess2 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess3 = int(input("Make a Guess: "))
        if guess3 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess3 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess4 = int(input("Make a Guess: "))
        if guess4 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess4 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess5 = int(input("Make a Guess: "))
        if guess5 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess5 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1
 
 
        guess6 = int(input("Make a Guess: "))
        if guess6 > number:
            print("Too High\n Guess Again.")
            turns -= 1
        elif guess6 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low.\nGuess Again.")
            turns -= 1


        guess7 = int(input("Make a Guess: "))
        if guess7 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess7 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess8 = int(input("Make a Guess: "))
        if guess8 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess8 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess9 = int(input("Make a Guess: "))
        if guess9 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess9 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1


        guess10 = int(input("Make a Guess: "))
        if guess10 > number:
            print("Too High\n Guess Again")
            turns -= 1
        elif guess10 == number:
            print("You Win")
            end = True
            turns = 0
            return
        else:
            print("Too Low\n Guess Again")
            turns -= 1
    else:
        os.system("cls")

if input("Would  you like to play easy or hard?") == "easy":
    print("You have 10 attempts to guess the number.")
    easy()
else:
    print("You have 5 attempts to guess the number.")
    hard()