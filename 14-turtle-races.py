# Turtle Races

import random
import turtle

FINISH_LINE = 300

# Setup window and turtles
window = turtle.Screen()
window.bgcolor("lightgreen")

ben = turtle.Turtle()
ben.color("blue")
ben.shape("turtle")
ben.penup()

mayda = turtle.Turtle()
mayda.color("purple")
mayda.shape("turtle")
mayda.penup()

ref = turtle.Turtle()
ref.pensize(4)

# Send turtles to starting locations
ben.goto(-300, 75)
mayda.goto(-300, -75)

# Draw the finish line
ref.penup()
ref.goto(FINISH_LINE, 100)
ref.pendown()
ref.goto(FINISH_LINE, -100)
ref.hideturtle()

# start racing
while ben.xcor() < FINISH_LINE and mayda.xcor() < FINISH_LINE:
    ben_step_size = random.randrange(1, 10)
    mayda_step_size = random.randrange(1, 10)
    
    ben.forward(ben_step_size)
    mayda.forward(mayda_step_size)

# somebody finished the race
if ben.xcor() > mayda.xcor():
    ben.write("Ben FTW!", move=False, align="right", font=("Arial", 24, "normal"))
    
elif mayda.xcor() > ben.xcor():
    mayda.write("Mayda FTW!", move=False, align="right", font=("Arial", 24, "normal"))
    
else:
    mayda.write("It's a tie!", move=False, align="right", font=("Arial", 24, "normal"))
    ben.write("It's a tie!", move=False, align="right", font=("Arial", 24, "normal"))


