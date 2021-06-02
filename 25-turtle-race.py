# Turtle Race
# Dan Schellenberg
# June 2, 2021

import turtle
import random

FINISH_LINE = 250
STARTING_POSITION = -250

# setup the window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

# setup the turtles
daniel = turtle.Turtle()
daniel.penup()
daniel.shape("turtle")
daniel.color("orange")
daniel.goto(STARTING_POSITION, 50)

hannah = turtle.Turtle()
hannah.penup()
hannah.shape("turtle")
hannah.color("red")
hannah.goto(STARTING_POSITION, -50)

# draw the finish line
ref = turtle.Turtle()
ref.penup()
ref.goto(FINISH_LINE, 150)
ref.pensize(4)
ref.pendown()
ref.goto(FINISH_LINE, -150)
ref.hideturtle()

# make the turtles race!
while daniel.xcor() < FINISH_LINE and hannah.xcor() < FINISH_LINE:
    daniel_step = random.randrange(1, 10)
    hannah_step = random.randrange(1, 10)
    
    daniel.forward(daniel_step)
    hannah.forward(hannah_step)

#victory speech
if daniel.xcor() > hannah.xcor():
    daniel.write("Daniel FTW! ", move=False, align="right", font=("Arial", 28, "normal"))
elif daniel.xcor() < hannah.xcor():
    hannah.write("Hannah FTW! ", move=False, align="right", font=("Arial", 28, "normal"))
else:
    daniel.write("Tie! ", move=False, align="right", font=("Arial", 28, "normal"))
    hannah.write("Tie! ", move=False, align="right", font=("Arial", 28, "normal"))


