import turtle
import random

#declare constants
STARTING_LINE_X = -300
FINISH_LINE_X = 250
VERTICAL_GAP = 50
MINIMUM_SPEED = 1
MAXIMUM_SPEED = 11

#setup the window
window = turtle.Screen()
window.bgcolor("lightgreen")

#setup the turtles
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("red")
alex.penup()

jaden = turtle.Turtle()
jaden.shape("turtle")
jaden.color("blue")
jaden.penup()

referee = turtle.Turtle()
referee.penup()
referee.pensize(3)

# go to starting positions
alex.goto(STARTING_LINE_X, VERTICAL_GAP)
jaden.goto(STARTING_LINE_X, -VERTICAL_GAP)

# draw the finish line
referee.goto(FINISH_LINE_X, VERTICAL_GAP*2)
referee.pendown()
referee.goto(FINISH_LINE_X, -VERTICAL_GAP*2)
referee.hideturtle()

# time to race!
while alex.xcor() < FINISH_LINE_X and jaden.xcor() < FINISH_LINE_X:
    alex_step = random.randrange(MINIMUM_SPEED, MAXIMUM_SPEED)
    jaden_step = random.randrange(MINIMUM_SPEED, MAXIMUM_SPEED)

    alex.forward(alex_step)
    jaden.forward(jaden_step)


# declare the winner
if alex.xcor() > jaden.xcor():
    print("Alex FTW!")
    alex.write("Alex FTW! ", move=False, align='right', font=('Arial', 48, 'normal'))
    
elif jaden.xcor() > alex.xcor():
    print("Jaden FTW!")
    jaden.write("Jaden FTW! ", move=False, align='right', font=('Arial', 48, 'normal'))
    
else:
    print("Tie!")
    alex.write("Tie! ", move=False, align='right', font=('Arial', 48, 'normal'))
    jaden.write("Tie! ", move=False, align='right', font=('Arial', 48, 'normal'))
    




