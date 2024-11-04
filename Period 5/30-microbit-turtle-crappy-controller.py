import microbit
import turtle

window = turtle.Screen()
aidan = turtle.Turtle()
aidan.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    if x > 250:
        print("RIGHT!")
        aidan.forward(3)
    elif x < -250:
        print("LEFT!")
        aidan.backward(3)
    else:
        print("FLAT")
    
