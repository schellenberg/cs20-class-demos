#turtle race demo
import turtle
import random

#define constants
FINISH_LINE = 300
STARTING_POSITION = -350
VERTICAL_SPACING = 30
MIN_SPEED = 1
MAX_SPEED = 9

#setup the screen
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup the turtles
caleb = turtle.Turtle()
caleb.shape("turtle")
caleb.color("orange")
caleb.penup()

asher = turtle.Turtle()
asher.shape("turtle")
asher.color("blue")
asher.penup()

referee = turtle.Turtle()
referee.pensize(5)
referee.penup()

#draw the finish line
referee.goto(FINISH_LINE, 2*VERTICAL_SPACING)
referee.pendown()
referee.goto(FINISH_LINE, -2*VERTICAL_SPACING)
referee.hideturtle()

#move to starting line
caleb.goto(STARTING_POSITION, VERTICAL_SPACING)
asher.goto(STARTING_POSITION, -VERTICAL_SPACING)

#turtle race time!
while caleb.xcor() < FINISH_LINE or asher.xcor() < FINISH_LINE:
    caleb_step = random.randrange(MIN_SPEED, MAX_SPEED)
    asher_step = random.randrange(MIN_SPEED, MAX_SPEED)
    
    caleb.forward(caleb_step)
    asher.forward(asher_step)

