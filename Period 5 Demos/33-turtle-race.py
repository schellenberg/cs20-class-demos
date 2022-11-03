import turtle
import random

STARTING_LOCATION = -300
FINISH_LINE = 275

#setup window
window = turtle.Screen()
window.bgcolor("lightblue")

#setup turtles
dayton = turtle.Turtle()
dayton.color("purple")
dayton.shape("turtle")
dayton.penup()

azka = turtle.Turtle()
azka.color("green")
azka.shape("turtle")
azka.penup()

nohl = turtle.Turtle()
nohl.pensize(5)

#move to starting location
dayton.goto(STARTING_LOCATION, 50)
azka.goto(STARTING_LOCATION, -50)

#draw the finish line
nohl.penup()
nohl.goto(FINISH_LINE, 100)
nohl.pendown()
nohl.goto(FINISH_LINE, -100)
nohl.hideturtle()

#race
while dayton.xcor() < FINISH_LINE and azka.xcor() < FINISH_LINE:
    dayton_step = random.randrange(1, 10)
    azka_step = random.randrange(1, 10)
    
    dayton.forward(dayton_step)
    azka.forward(azka_step)

#celebration
if dayton.xcor() > azka.xcor():
    print("Dayton FTW!")
    dayton.write("Dayton FTW! ", False , align="right", font=('Arial', 50, 'normal'))

elif azka.xcor() > dayton.xcor():
    print("Azka FTW!")
    azka.write("Azka FTW! ", False , align="right", font=('Arial', 50, 'normal'))

else:
    print("Tie!")
    dayton.write("Tie! ", False , align="right", font=('Arial', 50, 'normal'))
    azka.write("Tie! ", False , align="right", font=('Arial', 50, 'normal'))
