# from turtle import Turtle, Screen
# timmy = Turtle()
# timmy.shape("turtle")
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.color("coral")
# print(timmy)
# timmy.forward(200)
# timmy.right(2000)


from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squrtile"])
table.add_column("Type", ["Electric", "Fire", "Water"])

table.align = "l"

print(table)



