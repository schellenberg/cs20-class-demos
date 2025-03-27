import turtle

# set up window
canvas = turtle.Screen()
canvas.bgcolor("lightblue")

#create rylan and set attributes
rylan = turtle.Turtle()
rylan.shape("turtle")
rylan.color("blue")
rylan.pensize(10)

#create mary and set attributes
mary = turtle.Turtle()
mary.color("green")
mary.pensize(3)

# draw a square with mary
for side in range(4):
    mary.right(90)
    mary.forward(100)

# draw a pentagon (5-sided shape) with rylan
for side in range(5):
    rylan.forward(200)
    rylan.left(360/5)
    
canvas.exitonclick()
