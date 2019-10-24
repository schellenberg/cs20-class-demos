import microbit
import time
import turtle

window = turtle.Screen()
corey = turtle.Turtle()

while True:
    x_tilt = microbit.accelerometer.get_x()
    if x_tilt < -200:
        print("LEFT!")
        corey.backward(5)
    elif x_tilt > 200:
        print("RIGHT!")
        corey.forward(5)
    time.sleep(0.1)