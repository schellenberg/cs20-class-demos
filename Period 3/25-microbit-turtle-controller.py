import microbit
import turtle

window = turtle.Screen()
hawraa = turtle.Turtle()
hawraa.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    if x > 200:
        print("RIGHT")
        microbit.display.show("R")
        hawraa.forward(5)
    elif x < -200:
        print("LEFT")
        microbit.display.show("L")
        hawraa.backward(5)
    else:
        print("FLAT")
        microbit.display.show("-")
