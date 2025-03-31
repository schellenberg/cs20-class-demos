import microbit
import turtle

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

mary = turtle.Turtle()
mary.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    # print(x)
    
    if x > 250:
        print("RIGHT!")
        mary.forward(5)
    elif x < -250:
        print("LEFT!")
        mary.backward(5)
    else:
        print("FLAT")