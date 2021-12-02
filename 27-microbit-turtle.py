import microbit
import time
import turtle

canvas = turtle.Screen()
bryce = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()
    #print(x)
    if x > 300:
        print("Right!")
        bryce.forward(5)
    elif x < -300:
        print("Left!")
        bryce.backward(5)
    
    #time.sleep(0.25)