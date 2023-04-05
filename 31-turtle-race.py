# turtle race

import turtle
import random

STARTING_LINE = -300
FINISH_LINE = 250

#setup window and turtles
window = turtle.Screen()
window.bgcolor("lightgreen")

jackson = turtle.Turtle()
jackson.shape("turtle")
jackson.color("blue")
jackson.penup()

jace = turtle.Turtle()
jace.shape("turtle")
jace.color("red")
jace.penup()

#draw the finish line
ref = turtle.Turtle()
ref.pensize(3)
ref.penup()
ref.goto(FINISH_LINE, 175)
ref.pendown()
ref.goto(FINISH_LINE, -175)
ref.hideturtle()

#send to start line
jackson.goto(STARTING_LINE, 100)
jace.goto(STARTING_LINE, -100)


# do the race!
while jackson.xcor() < FINISH_LINE and jace.xcor() < FINISH_LINE:
    jackson_step = random.randrange(1, 10)
    jace_step = random.randrange(1, 10)

    jackson.forward(jackson_step)
    jace.forward(jace_step)

#victory message
if jackson.xcor() > jace.xcor():
    jackson.write("Jackson FTW! ", False, "right", ("Arial", 32, "normal"))

elif jace.xcor() > jackson.xcor():
    jace.write("Jace FTW! ", False, "right", ("Arial", 32, "normal"))

else:
    jackson.write("Tie! ", False, "right", ("Arial", 32, "normal"))
    jace.write("Tie! ", False, "right", ("Arial", 32, "normal"))