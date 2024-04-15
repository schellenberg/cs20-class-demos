import turtle

# setting up the window
the_window = turtle.Screen()
the_window.bgcolor("lightgreen")

# setup a turtle
chase = turtle.Turtle()
chase.shape("turtle")
chase.color("burlywood")
chase.pensize(10)

# setup another turtle
ella = turtle.Turtle()
ella.pensize(8)
ella.shape("turtle")

# setup yet one more turtle
mouad = turtle.Turtle()
mouad.pensize(13)
mouad.shape("turtle")
mouad.color("blue")

# go get ready to draw a triangle
ella.penup()
ella.backward(250)
ella.pendown()

# go get ready to draw a square
mouad.penup()
mouad.backward(150)
mouad.right(90)
mouad.forward(250)
mouad.left(90)
mouad.pendown()

# draw a pentagon
for side in range(5):
    chase.forward(200)
    chase.left(360/5)
    
    
# draw a triangle
for side in range(3):
    ella.forward(150)
    ella.left(360/3)


# draw a square
for the_color in ["blue", "green", "yellow", "red"]:
    mouad.color(the_color)
    mouad.forward(150)
    mouad.left(360/4)
    
    
    
    