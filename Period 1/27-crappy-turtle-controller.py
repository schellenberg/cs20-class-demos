import microbit
import turtle

window = turtle.Screen()
sensi = turtle.Turtle()
sensi.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    if x > 200:
        print("RIGHT")
        sensi.forward(5)
    elif x < -200:
        print("LEFT")
        sensi.backward(5)
    else:
        print("FLAT")