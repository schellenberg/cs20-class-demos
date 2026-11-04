import microbit
import turtle

window = turtle.Screen()
isaac = turtle.Turtle()
isaac.shape("turtle")
isaac.color("green")

while True:
    x = microbit.accelerometer.get_x()
    if x > 500:
        print("RIGHT!")
        microbit.display.show(">")
        isaac.forward(5)
    elif x < -500:
        print("LEFT!")
        microbit.display.show("<")
        isaac.backward(5)
    else:
        print("Not tilted")
        microbit.display.show("-")
        
