import turtle
import microbit

canvas = turtle.Screen()
afnan = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()
    print(f'x: {x}')

    if x > 300:
        print("RIGHT!")
        afnan.forward(5)
        
    elif x < -300:
        print("LEFT!")
        afnan.backward(5)
        