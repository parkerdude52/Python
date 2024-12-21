print("Welcome to the rollercoaster")
height = int(input("What is your height in cm"))

if height >= 120:
    print("You can ride the coaster!")
    age = int(input("What is your age"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    photo = input("Do you want a photo taken? Y or N.")
    if photo == "Y":
        bill += 3

    print(f"your final bill is ${bill}.")

else:
    print("sorry, you have to grow taller before you can ride this ride.")
