import turtle
import random

STARTING_X_COORDINATE = -250
VERTICAL_BUFFER = 50
FINISH_LINE = 225

#setup window
the_canvas = turtle.Screen()
the_canvas.bgcolor("lightgreen")

#setup the turtles
albert = turtle.Turtle()
albert.shape("turtle")
albert.color("blue")
albert.penup()

michael = turtle.Turtle()
michael.shape("turtle")
michael.color("red")
michael.penup()

referee = turtle.Turtle()
referee.pensize(5)
referee.penup()

#send turtles to the start
albert.goto(STARTING_X_COORDINATE, VERTICAL_BUFFER)
michael.goto(STARTING_X_COORDINATE, -VERTICAL_BUFFER)

#draw the finish line
referee.goto(FINISH_LINE, VERTICAL_BUFFER * 2)
referee.pendown()
referee.goto(FINISH_LINE, -VERTICAL_BUFFER * 2)
referee.hideturtle()

#have the turtles race!
while albert.xcor() < FINISH_LINE and michael.xcor() < FINISH_LINE:
    albert_step = random.randrange(1, 8)
    michael_step = random.randrange(1, 8)
    
    albert.forward(albert_step)
    michael.forward(michael_step)
    
    
if albert.xcor() > michael.xcor():
    print("Albert FTW!")
    albert.write("Albert FTW!  ", align="right", font=("Arial", 50, "normal"))
    
elif michael.xcor() > albert.xcor():
    print("Michael FTW!")
    michael.write("Michael FTW!  ", align="right", font=("Arial", 50, "normal"))
    
else:
    print("Tie!")
    albert.write("Tie!  ", align="right", font=("Arial", 50, "normal"))
    michael.write("Tie!  ", align="right", font=("Arial", 50, "normal"))
    
    
    