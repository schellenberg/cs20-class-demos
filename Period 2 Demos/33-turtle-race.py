# turtle race

import turtle
import random

STARTING_LINE = -300
FINISH_LINE = 250

# setup window
canvas = turtle.Screen()
canvas.bgcolor("lightblue")

# create turtles
natalie = turtle.Turtle()
natalie.color("purple")
natalie.shape("turtle")
natalie.penup()

erika = turtle.Turtle()
erika.color("violet")
erika.shape("turtle")
erika.penup()

abdul = turtle.Turtle()
abdul.pensize(5)
abdul.penup()

#move to starting locations
natalie.goto(STARTING_LINE, 100)
erika.goto(STARTING_LINE, -100)

#draw finish line
abdul.goto(FINISH_LINE, 150)
abdul.pendown()
abdul.goto(FINISH_LINE, -150)
abdul.hideturtle()

#race
while natalie.xcor() < FINISH_LINE and erika.xcor() < FINISH_LINE:
    natalie_step = random.randrange(1, 10)
    erika_step = random.randrange(1, 10)
    
    natalie.forward(natalie_step)
    erika.forward(erika_step)
    
#print a win screen message
if natalie.xcor() > erika.xcor():
    print("Natalie wins!")
    natalie.write("Natalie FTW! ", False, align="right", font=('Arial', 50, 'normal'))

elif erika.xcor() > natalie.xcor():
    print("Erika wins!")
    erika.write("Erika FTW! ", False, align="right", font=('Arial', 50, 'normal'))

else:
    print("Tie!")
    natalie.write("Tie! ", False, align="right", font=('Arial', 50, 'normal'))
    erika.write("Tie! ", False, align="right", font=('Arial', 50, 'normal'))


