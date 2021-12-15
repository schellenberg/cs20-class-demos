import turtle
import random
import microbit
import time

STARTING_LINE = -250
FINISH_LINE = 250

window = turtle.Screen()
window.bgcolor("lightblue")

#create turtles and go to starting location
uday = turtle.Turtle()
uday.color("purple")
uday.penup()
uday.shape("turtle")
uday.goto(STARTING_LINE, -50)

alex = turtle.Turtle()
alex.color("green")
alex.penup()
alex.shape("turtle")
alex.goto(STARTING_LINE, 50)

# draw finish line
ref = turtle.Turtle()
ref.penup()
ref.pensize(4)
ref.goto(FINISH_LINE, 100)
ref.pendown()
ref.goto(FINISH_LINE, -100)
ref.hideturtle()

while uday.xcor() < FINISH_LINE or alex.xcor() < FINISH_LINE:
    uday_step = random.randrange(1, 8)
    alex_step = random.randrange(1, 8)

    time.sleep(0.05)
    if microbit.button_a.was_pressed():
        uday.forward(uday_step)
    if microbit.button_b.was_pressed():
        alex.forward(alex_step)

if uday.xcor() > alex.xcor():
    uday.write("Uday FTW! ", move=False, align='right', font=('Arial', 45, 'normal'))
elif uday.xcor() < alex.xcor():
    alex.write("Alex FTW! ", move=False, align='right', font=('Arial', 45, 'normal'))
else:
    uday.write("Tie! ", move=False, align='right', font=('Arial', 45, 'normal'))
    alex.write("Tie! ", move=False, align='right', font=('Arial', 45, 'normal'))
    
