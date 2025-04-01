import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

ayaan = turtle.Turtle()
ayaan.color("green")
ayaan.shape("turtle")
ayaan.pensize(10)

#penup and pendown
# ayaan.forward(50)
# ayaan.penup()
# ayaan.forward(25)
# ayaan.pendown()
# ayaan.forward(50)

# ayaan.forward(-100)
# ayaan.left(-45)
# ayaan.backward(-100)


#spiral shape
ayaan.penup()
ayaan.speed(0)
for step in range(5, 200, 2):
    ayaan.stamp()
    ayaan.forward(step)
    ayaan.right(30)


