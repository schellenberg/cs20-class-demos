import microbit
import time
import turtle

canvas = turtle.Screen()

jack = turtle.Turtle()
jack.color("blue")

while True:
    x = microbit.accelerometer.get_x()
    
    if x > 300:
        print("RIGHT")
        jack.forward(30)
    
    elif x < -300:
        print("LEFT")
        jack.backward(30)
    
    #time.sleep(0.5)
