#turtle race demo
import turtle
import random

#define global variables
FINISH_LINE = 300
STARTING_POSITION = -350
VERTICAL_SPACE = 50

#setup the screen
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup the turtles
rennata = turtle.Turtle()
rennata.color("pink")
rennata.shape("turtle")
rennata.penup()

amrita = turtle.Turtle()
amrita.color("blue")
amrita.shape("turtle")
amrita.penup()

referee = turtle.Turtle()
referee.pensize(5)
referee.penup()
referee.speed(0)

#draw the finish line
referee.goto(FINISH_LINE, 2 * VERTICAL_SPACE)
referee.pendown()
referee.goto(FINISH_LINE, -2 * VERTICAL_SPACE)
referee.hideturtle()

#move to starting locations
rennata.goto(STARTING_POSITION, VERTICAL_SPACE)
amrita.goto(STARTING_POSITION, -VERTICAL_SPACE)


#turtle race time!

while rennata.xcor() < FINISH_LINE or amrita.xcor() < FINISH_LINE:
    rennata_step = random.randrange(1, 10)
    amrita_step = random.randrange(1, 10)

    rennata.forward(rennata_step)
    amrita.forward(amrita_step)
    

