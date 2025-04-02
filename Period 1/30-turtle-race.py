import turtle
import random

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
while mehreeb.xcor() < FINISH_LINE_X and zara.xcor() < FINISH_LINE_X:
    mehreeb_step = random.randrange(1, 7)
    zara_step = random.randrange(1, 7)

    mehreeb.forward(mehreeb_step)
    zara.forward(zara_step)


#who's the winner?
if mehreeb.xcor() > zara.xcor():
    print("Mehreeb wins!")
    mehreeb.write("Mehreeb FTW! ", False, align="right", font=('Arial', 50, 'normal'))
elif zara.xcor() > mehreeb.xcor():
    print("Zara wins!")
    zara.write("Zara FTW! ", False, align="right", font=('Arial', 50, 'normal'))
else:
    print("It's a tie!")
    mehreeb.write("Tie! ", False, align="right", font=('Arial', 50, 'normal'))
    zara.write("Tie! ", False, align="right", font=('Arial', 50, 'normal'))

