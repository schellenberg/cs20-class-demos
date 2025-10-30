import turtle
import random

#defining constants
STARTING_X_POSITION = -300
VERTICAL_SPACING = 100
FINISH_LINE_X = 300

# set up the window
window = turtle.Screen()
window.bgcolor("lightgreen")

# set up the turtles
ali = turtle.Turtle()
ali.color("red")
ali.shape("turtle")
ali.penup()

shy = turtle.Turtle()
shy.color("blue")
shy.shape("turtle")
shy.penup()

referee = turtle.Turtle()
referee.pensize(3)

#goto starting spots
ali.goto(STARTING_X_POSITION, VERTICAL_SPACING)
shy.goto(STARTING_X_POSITION, -VERTICAL_SPACING)

#draw finish line
referee.penup()
referee.goto(FINISH_LINE_X, 2*VERTICAL_SPACING)
referee.pendown()
referee.goto(FINISH_LINE_X, -2*VERTICAL_SPACING)
referee.hideturtle()

#race time!
while ali.xcor() < FINISH_LINE_X and shy.xcor() < FINISH_LINE_X:
    ali_step = random.randrange(1, 10)
    shy_step = random.randrange(1, 10)

    ali.forward(ali_step)
    shy.forward(shy_step)

#who's the winner?
if ali.xcor() > shy.xcor():
    print("Ali FTW!")
    ali.write("Ali FTW!  ", False, align="right", font=("Arial", 40, "normal"))
elif shy.xcor() > ali.xcor():
    print("Shy FTW!")
    shy.write("Shy FTW!  ", False, align="right", font=("Arial", 40, "normal"))
else:
    print("Tie")
    ali.write("Tie!  ", False, align="right", font=("Arial", 40, "normal"))
    shy.write("Tie!  ", False, align="right", font=("Arial", 40, "normal"))





