import turtle
import random

# define constants
FINISH_LINE_X = 250
STARTING_X_POSITION = -300
VERTICAL_SEPARATION = 75
MINIMUM_SPEED = 1
MAXIMUM_SPEED = 7

# create screen
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

# create the turtles
ben = turtle.Turtle()
ben.shape("turtle")
ben.penup()
ben.color("orange")

steven = turtle.Turtle()
steven.shape("turtle")
steven.penup()
steven.color("purple")

ref = turtle.Turtle()
ref.penup()
ref.pensize(3)

#go draw finish line
ref.goto(FINISH_LINE_X, VERTICAL_SEPARATION * 2)
ref.pendown()
ref.goto(FINISH_LINE_X, -VERTICAL_SEPARATION * 2)
ref.hideturtle()

# head to starting points
ben.goto(STARTING_X_POSITION, VERTICAL_SEPARATION)
steven.goto(STARTING_X_POSITION, -VERTICAL_SEPARATION)

#race time!
while ben.xcor() < FINISH_LINE_X and steven.xcor() < FINISH_LINE_X:
    ben_step = random.randrange(MINIMUM_SPEED, MAXIMUM_SPEED)
    steven_step = random.randrange(MINIMUM_SPEED, MAXIMUM_SPEED)

    ben.forward(ben_step)
    steven.forward(steven_step)

# declare the victor
if steven.xcor() > ben.xcor():
    print("Steven FTW!")
    steven.write("Steven FTW! ", move=False, align='right', font=('Arial', 48, 'normal'))
    
elif ben.xcor() > steven.xcor():
    print("Ben FTW!")
    ben.write("Ben FTW! ", move=False, align='right', font=('Arial', 48, 'normal'))
    
else:
    print("It's a tie!")
    steven.write("Tie! ", move=False, align='right', font=('Arial', 48, 'normal'))
    ben.write("Tie! ", move=False, align='right', font=('Arial', 48, 'normal'))
    