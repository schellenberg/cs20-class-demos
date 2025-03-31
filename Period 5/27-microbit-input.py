import microbit
import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

gavin = turtle.Turtle()
gavin.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    # print(x)
    if x > 500:
        print("RIGHT!")
        gavin.forward(5)
    elif x < -500:
        print("LEFT!")
        gavin.backward(5)
    else:
        print("FLAT")
