import turtle
import microbit

canvas = turtle.Screen()
jackson = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()
    
    print(f'x: {x}')
    
    if x > 200:
        print("RIGHT!")
        jackson.forward(5)
    
    elif x < -200:
        print("LEFT!")
        jackson.backward(5)