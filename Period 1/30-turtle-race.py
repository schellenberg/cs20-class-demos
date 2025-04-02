import turtle

#declare constants
STARTING_X_LOCATION = -250
VERTICAL_SPACING = 50
FINISH_LINE_X = 275

#setup window and turtles
window = turtle.Screen()
window.bgcolor("lightblue")

mehreeb = turtle.Turtle()
mehreeb.color("darkblue")
mehreeb.shape("turtle")
mehreeb.penup()

zara = turtle.Turtle()
zara.color("green")
zara.shape("turtle")
zara.penup()

referee = turtle.Turtle()
referee.pensize(7)

#head to starting locations
mehreeb.goto(STARTING_X_LOCATION, VERTICAL_SPACING)
zara.goto(STARTING_X_LOCATION, -VERTICAL_SPACING)

#draw the finish line
referee.penup()
referee.goto(FINISH_LINE_X, VERTICAL_SPACING * 2.5)
referee.pendown()
referee.goto(FINISH_LINE_X, -VERTICAL_SPACING * 2.5)
referee.hideturtle()

#turtle race time!



