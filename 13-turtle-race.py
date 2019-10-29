# Turtle Race

import turtle
import random

FINISH_LINE = 250

canvas = turtle.Screen()
canvas.bgcolor("red")

# initialize turtles
caid = turtle.Turtle()
caid.color("blue")
caid.shape("turtle")
caid.penup()

tyson = turtle.Turtle()
tyson.color("green")
tyson.shape("turtle")
tyson.penup()

ref = turtle.Turtle()
ref.pensize(5)

# go to starting locations
caid.goto(-250, 50)
tyson.goto(-250, -50)

# draw the finish line
ref.penup()
ref.goto(FINISH_LINE, 150)
ref.pendown()
ref.goto(FINISH_LINE, -150)
ref.hideturtle()

# run the race!!!
while caid.xcor() < FINISH_LINE and tyson.xcor() < FINISH_LINE:
    caid_step_size = random.randrange(1, 5)
    tyson_step_size = random.randrange(1, 5)

    caid.forward(caid_step_size)
    tyson.forward(tyson_step_size)

# display winner text
if caid.xcor() > tyson.xcor():
    caid.write("Caid FTW! ", True, align="right", font=("Arial", 42, "bold"))

elif caid.xcor() < tyson.xcor():
    tyson.write("Tyson FTW! ", True, align="right", font=("Arial", 42, "bold"))

else:
    caid.write("Tie! ", True, align="right", font=("Arial", 42, "bold"))
    tyson.write("Tie! ", True, align="right", font=("Arial", 42, "bold"))
