import os
end = False
def game():

    print("""
        d8888b.  .d8b.  d8b   db d8888b.      d8b   db  .d8b.  .88b  d88. d88888b 
        88  `8D d8' `8b 888o  88 88  `8D      888o  88 d8' `8b 88'YbdP`88 88'     
        88oooY' 88ooo88 88V8o 88 88   88      88V8o 88 88ooo88 88  88  88 88ooooo 
        88~~~b. 88~~~88 88 V8o88 88   88      88 V8o88 88~~~88 88  88  88 88~~~~~ 
        88   8D 88   88 88  V888 88  .8D      88  V888 88   88 88  88  88 88.     
        Y8888P' YP   YP VP   V8P Y8888D'      VP   V8P YP   YP YP  YP  YP Y88888P 
                                                                            
                                                                            
        d888b  d88888b d8b   db d88888b d8888b.  .d8b.  d888888b  .d88b.  d8888b.
        88' Y8b 88'     888o  88 88'     88  `8D d8' `8b `~~88~~' .8P  Y8. 88  `8D
        88      88ooooo 88V8o 88 88ooooo 88oobY' 88ooo88    88    88    88 88oobY'
        88  ooo 88~~~~~ 88 V8o88 88~~~~~ 88`8b   88~~~88    88    88    88 88`8b  
        88. ~8~ 88.     88  V888 88.     88 `88. 88   88    88    `8b  d8' 88 `88.
        Y888P  Y88888P VP   V8P Y88888P 88   YD YP   YP    YP     `Y88P'  88   YD""")

    name1 = input("What state do you live in? ")
    name2 = input("What's the breed of your first pet? ")

    print(f"Your Band name could be: The {name1} {name2}s")

    if input("Would you like to play again? Type 'y' or 'n'.") == 'n':
        end = True

while end == False:
    game()
else:
    os.system("cls")
