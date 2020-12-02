# Turtle Race

import turtle
import random

STARTING_LOCATION_X = -300
FINISH_LINE_X = 300

#setup window
window = turtle.Screen()

#setup turtles
arjun = turtle.Turtle()
arjun.color("blue")
arjun.shape("turtle")
arjun.penup()

waleejah = turtle.Turtle()
waleejah.color("red")
waleejah.shape("turtle")
waleejah.penup()

referee = turtle.Turtle()
referee.hideturtle()
referee.pensize(4)

#draw finish line
referee.penup()
referee.goto(FINISH_LINE_X, 100)
referee.pendown()
referee.goto(FINISH_LINE_X, -100)

#send turtles to starting locations
arjun.goto(STARTING_LOCATION_X, 50)
waleejah.goto(STARTING_LOCATION_X, -50)



#race the turtles
while arjun.xcor() <= FINISH_LINE_X and waleejah.xcor() <= FINISH_LINE_X:
    arjun_step = random.randrange(1,7)
    waleejah_step = random.randrange(1,7)
    
    arjun.forward(arjun_step)
    waleejah.forward(waleejah_step)
   
   
if arjun.xcor() > waleejah.xcor():
    arjun.write("Arjun FTW! ", move=False, align="right", font=("Arial", 40, "normal"))

elif arjun.xcor() < waleejah.xcor():
    waleejah.write("Waleejah FTW! ", move=False, align="right", font=("Arial", 40, "normal"))

else:
    arjun.write("Tie! ", move=False, align="right", font=("Arial", 40, "normal"))
    waleejah.write("Tie! ", move=False, align="right", font=("Arial", 40, "normal"))