import microbit
import turtle
import time

canvas = turtle.Screen()
lucy = turtle.Turtle()

while True:
    x_tilt = microbit.accelerometer.get_x()
    
    if x_tilt > 200:
        print("Right")
        lucy.forward(5)
    
    elif x_tilt < -200:
        print("Left")
        lucy.backward(5)
    
    else:
        print("Flat")
    
    time.sleep(0.1)
