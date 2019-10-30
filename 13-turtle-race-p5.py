# Turtle Race!

import turtle
import random

FINISH_LINE = 275

# set up screen and turtles
canvas = turtle.Screen()
canvas.bgcolor("red")

amaad = turtle.Turtle()
amaad.color("black")
amaad.shape("turtle")
amaad.penup()

liam = turtle.Turtle()
liam.color("pink")
liam.shape("turtle")
liam.penup()

# send turtles to starting location
amaad.goto(-300, 100)
liam.goto(-300, -100)

# draw the finish line
ref = turtle.Turtle()
ref.pensize(4)
ref.penup()
ref.goto(FINISH_LINE, 150)
ref.pendown()
ref.goto(FINISH_LINE, -150)
ref.hideturtle()

# run the race!
while amaad.xcor() < FINISH_LINE and liam.xcor() < FINISH_LINE:
    amaad_step = random.randrange(1, 10)
    liam_step = random.randrange(1, 10)
    
    amaad.forward(amaad_step)
    liam.forward(liam_step)


# print out the winner
if amaad.xcor() > liam.xcor():
    amaad.write("Amaad wins! ", move=False, align="right", font=("Arial", 50, "normal"))
    
elif amaad.xcor() < liam.xcor():
    liam.write("Liam wins! ", move=False, align="right", font=("Arial", 50, "normal"))
    
else:
    amaad.write("Tie! ", move=False, align="right", font=("Arial", 50, "normal"))
    liam.write("Tie! ", move=False, align="right", font=("Arial", 50, "normal"))