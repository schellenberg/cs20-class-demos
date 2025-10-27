import microbit
import turtle

window = turtle.Screen()
chase = turtle.Turtle()
chase.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
#     print(x)
    
    if x > 200:
        print("RIGHT!")
        chase.forward(2)
    
    elif x < -200:
        print("LEFT!")
        chase.backward(2)
    
    else:
        print("FLAT")
