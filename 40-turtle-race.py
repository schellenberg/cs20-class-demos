# Turtle Races

import turtle
import random

STARTING_X_POSITION = -300
FINISH_LINE_X_POSITION = 300

# setup window
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

# setup two turtles
anshu = turtle.Turtle()
anshu.color("red")
anshu.shape("turtle")
anshu.penup()

mitchell = turtle.Turtle()
mitchell.color("orange")
mitchell.shape("turtle")
mitchell.penup()

# make a referee and draw the finish line
referee = turtle.Turtle()
referee.pensize(4)
referee.penup()
referee.goto(FINISH_LINE_X_POSITION, 200)
referee.pendown()
referee.goto(FINISH_LINE_X_POSITION, -200)
referee.hideturtle()

# send to starting line
anshu.goto(STARTING_X_POSITION, 100)
mitchell.goto(STARTING_X_POSITION, -100)

# race time!
while anshu.xcor() <= FINISH_LINE_X_POSITION and mitchell.xcor() <= FINISH_LINE_X_POSITION:
    anshu_step = random.randrange(1, 7)
    mitchell_step = random.randrange(1, 8)
    
    anshu.forward(anshu_step)
    mitchell.forward(mitchell_step)

# print the winner
if anshu.xcor() > mitchell.xcor():
    anshu.write("Anshu FTW! ", move=False, align="right", font=("Arial", 50, "normal"))
elif anshu.xcor() < mitchell.xcor():
    mitchell.write("Mitchell FTW! ", move=False, align="right", font=("Arial", 50, "normal"))
else:
    anshu.write("Tie! ", move=False, align="right", font=("Arial", 50, "normal"))
    mitchell.write("Tie! ", move=False, align="right", font=("Arial", 50, "normal"))