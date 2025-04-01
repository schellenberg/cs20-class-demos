import turtle

window = turtle.Screen()
window.bgcolor("lightblue")

vaidehi = turtle.Turtle()
vaidehi.shape("turtle")
vaidehi.pensize(10)

# vaidehi.forward(-100)
# vaidehi.left(-45)
# vaidehi.backward(-50)

#penup and pendown
# vaidehi.forward(100)
# vaidehi.penup()
# vaidehi.forward(50)
# vaidehi.left(90)
# vaidehi.pendown()
# vaidehi.forward(100)

#spiral shape
vaidehi.penup()
vaidehi.speed(0)
for step in range(10, 150, 2):
    vaidehi.stamp()
    vaidehi.forward(step)
    vaidehi.right(30)

