import turtle
import random

STARTING_X_COORDINATE = -250
VERTICAL_BUFFER = 50
FINISH_LINE = 250

#setup the window
the_canvas = turtle.Screen()
the_canvas.bgcolor("lightgreen")

#setup the turtles
parker = turtle.Turtle()
parker.shape("turtle")
parker.color("blue")
parker.penup()

aliyaan = turtle.Turtle()
aliyaan.shape("turtle")
aliyaan.penup()

referee = turtle.Turtle()
referee.penup()
referee.pensize(5)

#send turtles to the start
parker.goto(STARTING_X_COORDINATE, VERTICAL_BUFFER)
aliyaan.goto(STARTING_X_COORDINATE, -VERTICAL_BUFFER)

#get the ref to draw the finish line
referee.goto(FINISH_LINE, VERTICAL_BUFFER * 2)
referee.pendown()
referee.goto(FINISH_LINE, VERTICAL_BUFFER * -2)
referee.hideturtle()

#have the race!
while parker.xcor() < FINISH_LINE and aliyaan.xcor() < FINISH_LINE:
    parker_step = random.randrange(1, 8)
    aliyaan_step = random.randrange(1, 8)
    
    parker.forward(parker_step)
    aliyaan.forward(aliyaan_step)


if parker.xcor() > aliyaan.xcor():
    print("Parker FTW!")
    parker.write("Parker FTW! ", move=False, align="right", font=("Arial", 50, "normal"))

elif aliyaan.xcor() > parker.xcor():
    print("Aliyaan FTW!")
    aliyaan.write("Aliyaan FTW! ", move=False, align="right", font=("Arial", 50, "normal"))
    
else:
    print("It's a tie!")
    parker.write("Tie! ", move=False, align="right", font=("Arial", 50, "normal"))
    aliyaan.write("Tie! ", move=False, align="right", font=("Arial", 50, "normal"))
