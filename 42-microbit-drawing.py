import microbit
import turtle

canvas = turtle.Screen()
sresta = turtle.Turtle()
sresta.shape("turtle")


while True:
    x = microbit.accelerometer.get_x()
    
    if x > 200:
        sresta.forward(1)
        
    elif x < -200:
        sresta.backward(1)
