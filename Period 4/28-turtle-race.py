import turtle
import random

#define constants
STARTING_X_POSITION = -300
VERTICAL_SPACING = 100
FINISH_LINE_X = 350

#setup screen
window = turtle.Screen()
window.bgcolor("lightgreen")

#setup turtles
poulomi = turtle.Turtle()
poulomi.color("red")
poulomi.shape("turtle")
poulomi.penup()

sadeem = turtle.Turtle()
sadeem.color("blue")
sadeem.shape("turtle")
sadeem.penup()

referee = turtle.Turtle()
referee.penup()
referee.pensize(3)

#goto starting positions
poulomi.goto(STARTING_X_POSITION, VERTICAL_SPACING)
sadeem.goto(STARTING_X_POSITION, -VERTICAL_SPACING)

#draw finish line
referee.goto(FINISH_LINE_X, 2*VERTICAL_SPACING)
referee.pendown()
referee.goto(FINISH_LINE_X, -2*VERTICAL_SPACING)
referee.hideturtle()

#racing time!
while poulomi.xcor() < FINISH_LINE_X and sadeem.xcor() < FINISH_LINE_X:
    poulomi_step = random.randrange(1, 10)
    sadeem_step = random.randrange(1, 10)
    
    poulomi.forward(poulomi_step)
    sadeem.forward(sadeem_step)

#who wins?
if poulomi.xcor() > sadeem.xcor():
    print("Poulomi FTW")
    poulomi.write("Poulomi FTW ", False, align="right", font=("Arial", 50, "normal"))
elif sadeem.xcor() > poulomi.xcor():
    print("Sadeem FTW")
    sadeem.write("Sadeem FTW ", False, align="right", font=("Arial", 50, "normal"))
else:
    print("Tie")
    poulomi.write("Tie ", False, align="right", font=("Arial", 50, "normal"))
    sadeem.write("Tie ", False, align="right", font=("Arial", 50, "normal"))
