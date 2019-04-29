import turtle


def turtles_are_touching(turtle1, turtle2, close_enough_distance):
    return False

window = turtle.Screen()
window.bgcolor("black")

mark = turtle.Turtle()
mark.color("red")
mark.penup()

shane = turtle.Turtle()
shane.color("green")
shane.penup()

mark.goto(200, 0)
shane.goto(-200, 5)
mark.left(180)

while not turtles_are_touching(mark, shane, 30):
    mark.forward(2)
    shane.forward(5)

print("Pretty close now...")