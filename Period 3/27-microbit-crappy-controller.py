import microbit
import turtle

the_window = turtle.Screen()
emily = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()

    if x > 200:
        print("RIGHT!")
        emily.forward(5)
    
    elif x < -200:
        print("LEFT!")
        emily.backward(5)

    else:
        print("FLAT")