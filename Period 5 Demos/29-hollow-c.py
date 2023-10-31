# hollow c demo

import turtle

#setup screen
canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

#setup turtle
avery = turtle.Turtle()
avery.pensize(5)
avery.color("red")

#first/basic solution
# avery.forward(175)
# avery.left(90)
# avery.forward(25)
# avery.left(90)
# avery.forward(200)
# avery.left(90)
# avery.forward(200)
# avery.left(90)
# avery.forward(200)
# avery.left(90)
# avery.forward(25)
# avery.left(90)
# avery.forward(175)
# avery.left(90)
# avery.forward(-150)
# avery.left(90)

#better solution
for side_length in [175, 25, 200, 200, 200, 25, 175, -150]:
    avery.forward(side_length)
    avery.left(90)
    
    