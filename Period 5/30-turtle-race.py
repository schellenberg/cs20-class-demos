import turtle
import random

#define constants
STARTING_X_LOCATION = -250
VERTICAL_SPACING = 50
FINISH_LINE_X = 275

#setup window and turtles
canvas = turtle.Screen()
canvas.bgcolor("lightblue")

ayman = turtle.Turtle()
ayman.color("red")
ayman.shape("turtle")
ayman.penup()

rafsan = turtle.Turtle()
rafsan.color("blue")
rafsan.shape("turtle")
rafsan.penup()

referee = turtle.Turtle()
referee.pensize(5)

#send to starting locations
ayman.goto(STARTING_X_LOCATION, VERTICAL_SPACING)
rafsan.goto(STARTING_X_LOCATION, -VERTICAL_SPACING)

#draw the finish line
referee.penup()
referee.goto(FINISH_LINE_X, VERTICAL_SPACING * 2)
referee.pendown()
referee.goto(FINISH_LINE_X, -VERTICAL_SPACING * 2)
referee.hideturtle()

#turtle race time!
while ayman.xcor() < FINISH_LINE_X and rafsan.xcor() < FINISH_LINE_X:
    ayman_step = random.randrange(1, 8)
    rafsan_step = random.randrange(1, 8)

    ayman.forward(ayman_step)
    rafsan.forward(rafsan_step)

#who's the winner?
if ayman.xcor() > rafsan.xcor():
    print("Ayman FTW!")
    ayman.write("Ayman FTW! ", False, align="right", font=("Arial", 50, "normal"))
elif rafsan.xcor() > ayman.xcor():
    print("Rafsan FTW!")
    rafsan.write("Rafsan FTW! ", False, align="right", font=("Arial", 50, "normal"))
else:
    print("It's a tie!")
    ayman.write("Tie! ", False, align="right", font=("Arial", 50, "normal"))
    rafsan.write("Tie! ", False, align="right", font=("Arial", 50, "normal"))
    
    

