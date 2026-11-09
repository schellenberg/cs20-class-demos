#turtle race demo
import turtle
import random

#declare constants
FINISH_LINE = 300
STARTING_LINE = -250
VERTICAL_OFFSET = 75
SMALLEST_STEP_SIZE = 1
LARGEST_STEP_SIZE = 12

#setup window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup the turtles
yulin = turtle.Turtle()
yulin.color("blue")
yulin.shape("turtle")
yulin.penup()

arash = turtle.Turtle()
arash.color("red")
arash.shape("turtle")
arash.penup()

#make the finish line
referee = turtle.Turtle()
referee.pensize(3)
referee.penup()
referee.goto(FINISH_LINE, 2*VERTICAL_OFFSET)
referee.pendown()
referee.goto(FINISH_LINE, -2*VERTICAL_OFFSET)
referee.hideturtle()

#head to starting locations
yulin.goto(STARTING_LINE, VERTICAL_OFFSET)
arash.goto(STARTING_LINE, -VERTICAL_OFFSET)

#start the race!

while yulin.xcor() < FINISH_LINE or arash.xcor() < FINISH_LINE:
    yulin_step = random.randrange(SMALLEST_STEP_SIZE, LARGEST_STEP_SIZE)
    arash_step = random.randrange(SMALLEST_STEP_SIZE, LARGEST_STEP_SIZE)

    yulin.forward(yulin_step)
    arash.forward(arash_step)


