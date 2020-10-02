
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

esther = turtle.Turtle()
esther.color("blue")
esther.shape("turtle")
esther.pensize(5)

for hour in range(12):
    #draw one tick mark
    esther.penup()
    esther.forward(100)
    esther.pendown()
    esther.forward(20)
    esther.penup()
    esther.forward(20)
    esther.stamp()
    esther.backward(140)
    esther.left(360/12)
    
