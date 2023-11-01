import turtle
import random

STARTING_LINE = -250
FINISH_LINE = 250
Y_OFFSET = 100 #how far from the center is the turtle?

#setup screen
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup turtles and head to start
muneeb = turtle.Turtle()
muneeb.penup()
muneeb.shape("turtle")
muneeb.color("blue")
muneeb.goto(STARTING_LINE, Y_OFFSET)

omar = turtle.Turtle()
omar.color("red")
omar.shape("turtle")
omar.penup()
omar.goto(STARTING_LINE, -Y_OFFSET)

#setup finish line
referee = turtle.Turtle()
referee.penup()
referee.goto(FINISH_LINE, -Y_OFFSET*2)
referee.pendown()
referee.goto(FINISH_LINE, Y_OFFSET*2)
referee.hideturtle()


#turtle race time!

while muneeb.xcor() < FINISH_LINE and omar.xcor() < FINISH_LINE:
    muneeb_step = random.randrange(1, 10)
    omar_step = random.randrange(1, 10)
    
    muneeb.forward(muneeb_step)
    omar.forward(omar_step)


if muneeb.xcor() > omar.xcor():
    print("Muneeb FTW!")
    muneeb.write("Muneeb FTW! ", move=False, align='right', font=('Arial', 40, 'normal'))

elif omar.xcor() > muneeb.xcor():
    print("Omar FTW!")
    omar.write("Omar FTW! ", move=False, align='right', font=('Arial', 40, 'normal'))
else:
    print("Tie!")
    muneeb.write("Tie! ", move=False, align='right', font=('Arial', 40, 'normal'))
    omar.write("Tie! ", move=False, align='right', font=('Arial', 40, 'normal'))





