import microbit
import turtle

window = turtle.Screen()
jiya = turtle.Turtle()
jiya.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    
    if x > 200:
        print("RIGHT!")
        jiya.forward(3)
    elif x < -200:
        print("LEFT!")
        jiya.backward(3)
    else:
        print("FLAT")

