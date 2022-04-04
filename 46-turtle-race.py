import turtle
import random

STARTING_LINE = -250
FINISH_LINE = 250

#setup window
window = turtle.Screen()
window.bgcolor("lightyellow")

#turtles setup on left side of window
sam = turtle.Turtle()
sam.shape("turtle")
sam.color("red")
sam.penup()
sam.goto(STARTING_LINE, 50)

aj = turtle.Turtle()
aj.shape("turtle")
aj.color("green")
aj.penup()
aj.goto(STARTING_LINE, -50)

#draw the finish line
ref = turtle.Turtle()
ref.penup()
ref.goto(FINISH_LINE, 100)
ref.pensize(4)
ref.pendown()
ref.goto(FINISH_LINE, -100)
ref.hideturtle()

#run the race!
while sam.xcor() < FINISH_LINE and aj.xcor() < FINISH_LINE:
    sams_step = random.randrange(1, 10)
    ajs_step = random.randrange(1, 10)

    #if sam.xcor() < FINISH_LINE:
    sam.forward(sams_step)
    #if aj.xcor() < FINISH_LINE:
    aj.forward(ajs_step)

#show a winning message
if sam.xcor() > aj.xcor():
    sam.write("Sam FTW!   ", False, align="right", font=("Arial", 42, "normal"))

elif sam.xcor() < aj.xcor():
    aj.write("AJ FTW!   ", False, align="right", font=("Arial", 42, "normal"))

else:
    sam.write("Tie!   ", False, align="right", font=("Arial", 42, "normal"))
    aj.write("Tie!   ", False, align="right", font=("Arial", 42, "normal"))
    
