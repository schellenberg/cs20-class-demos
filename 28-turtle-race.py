# turtle race

import turtle
import random

FINISH_LINE = 350

# define window to draw on
window = turtle.Screen()
window.bgcolor("black")

# create the turtles
kieran = turtle.Turtle()
kieran.shape("turtle")
kieran.color("yellow")
kieran.penup()

dan = turtle.Turtle()
dan.shape("turtle")
dan.color("red")
dan.penup()

ref = turtle.Turtle()
ref.color("white")
ref.penup()
ref.pensize(5)

# draw finish line
ref.goto(FINISH_LINE, 150)
ref.pendown()
ref.goto(FINISH_LINE, -150)
ref.hideturtle()

# send turtles to start
kieran.goto(-350, 50)
dan.goto(-350, -50)

while kieran.xcor() <= FINISH_LINE and dan.xcor() <= FINISH_LINE:
    kieran_step = random.randrange(1,5)
    dan_step = random.randrange(1,5)
    
    kieran.forward(kieran_step)
    dan.forward(dan_step)


if kieran.xcor() > dan.xcor():
    print("Kieran FTW!")
    kieran.write("Kieran FTW!", move=False, align="right", font=("Arial", 40, "normal"))
elif dan.xcor() > kieran.xcor():
    print("Dan FTW!")
    dan.write("Dan FTW!", move=False, align="right", font=("Arial", 40, "normal"))
else:
    print("It's a tie!")
    ref.write("Tie!", move=False, align="right", font=("Arial", 40, "normal"))
