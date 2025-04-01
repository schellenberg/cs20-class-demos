# hollow c

import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightblue")

harjot = turtle.Turtle()
harjot.shape("turtle")
harjot.pensize(5)

#first method
# harjot.forward(200)
# harjot.right(-90)
# harjot.forward(40)
# harjot.right(-90)
# harjot.forward(160)
# harjot.right(90)
# harjot.forward(120)
# harjot.right(90)
# harjot.forward(160)
# harjot.right(-90)
# harjot.forward(40)
# harjot.right(-90)
# harjot.forward(200)
# harjot.right(-90)
# harjot.forward(200)
# harjot.right(-90)

#second method -- for loops
# for length in [200, 50, 250, 300, 250, 50, 200]:
#     harjot.forward(length)
#     harjot.left(90)
#     
# harjot.right(180)
# harjot.forward(200)

#third method -- better for loops
for length in [200, 50, 250, 300, 250, 50, 200, -200]:
    harjot.forward(length)
    harjot.left(90)
    

