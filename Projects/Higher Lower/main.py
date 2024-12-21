import random
from game_data import data
from art import logo, vs
import os
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name},  {account_descr}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_continue = True
accountB = random.choice(data)

while game_continue:
    
    
    
    accountA = accountB
    accountB = random.choice(data)

    if accountA == accountB:
        personB = random.choice(data)

    print(f"compare A: {format_data(accountA)}")
    print(vs)
    print(f"compare B: {format_data(accountB)}")

    guess = input("Who has more subscribers? Type 'A' or 'B'").lower()

    a_follower_count = accountA["follower_count"]
    b_follower_count = accountB["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("cls")
    print(logo)

    if is_correct:
        score +=1
        print(f"You're Right! Current score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


