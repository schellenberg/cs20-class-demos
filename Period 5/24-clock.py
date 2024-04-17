import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

jack = turtle.Turtle()
jack.shape("turtle")
jack.color("blue")
jack.pensize(5)

for hour in range(12):
    # draw one hour tick mark
    jack.penup()
    jack.forward(130)
    jack.pendown()
    jack.forward(20)
    jack.penup()
    jack.forward(20)
    jack.stamp()
    jack.backward(170)

    jack.right(360/12)
