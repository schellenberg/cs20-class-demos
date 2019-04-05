import microbit
import time
import turtle

canvas = turtle.Screen()
canvas.bgcolor("black")

sage = turtle.Turtle()
sage.color("pink")
sage.shape("turtle")

# infinite loop to run on the microbit
while True:
    x = microbit.accelerometer.get_x()
    if x > 200:
        print("Right")
        microbit.display.show("R")
        sage.forward(5)
    elif x < -200:
        print("Left")
        microbit.display.show("L")
        sage.backward(5)
    else:
        print("Straight")
        microbit.display.show("-")
    time.sleep(0.1)