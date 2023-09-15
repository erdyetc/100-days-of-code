from turtle import Turtle, Screen
import prettytable

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# #documentation: https://docs.python.org/3/library/turtle.html#turtle.forward
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick() 

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
print(table.align)
table.align = "l"
print(table)