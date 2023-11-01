import turtle
import random

STARTING_LINE = -275
FINISH_LINE = 275

#setup window
window = turtle.Screen()
window.bgcolor("lightgreen")

#setup racing turtles
nissa = turtle.Turtle()
nissa.shape("turtle")
nissa.color("purple")
nissa.penup()
#nissa.speed(0)

angadveer = turtle.Turtle()
angadveer.shape("turtle")
angadveer.color("blue")
angadveer.penup()
#angadveer.speed(0)

#setup finish line
referee = turtle.Turtle()
referee.penup()
referee.goto(FINISH_LINE, 100)
referee.pendown()
referee.goto(FINISH_LINE, -100)
referee.hideturtle()

#send them to starting locations
nissa.goto(STARTING_LINE, 50)
angadveer.goto(STARTING_LINE, -50)

# race the turtles!
while nissa.xcor() < FINISH_LINE and angadveer.xcor() < FINISH_LINE:
    nissa_step = random.randrange(1, 10)
    angadveer_step = random.randrange(1, 10)
    
    nissa.forward(nissa_step)
    angadveer.forward(angadveer_step)


if angadveer.xcor() > nissa.xcor():
    angadveer.write("I win!  ", move=False, align='right', font=('Arial', 30, 'normal'))

elif nissa.xcor() > angadveer.xcor():
    nissa.write("I win!  ", move=False, align='right', font=('Arial', 30, 'normal'))

else:
    angadveer.write("Tie!  ", move=False, align='right', font=('Arial', 30, 'normal'))
    nissa.write("Tie!  ", move=False, align='right', font=('Arial', 30, 'normal'))
    
