import microbit
import turtle

window = turtle.Screen()
david = turtle.Turtle()

while True:
    x_tilt = microbit.accelerometer.get_x()
    
    if x_tilt > 200:
        print("RIGHT!")
        david.forward(5)
    
    elif x_tilt < -200:
        print("LEFT!")
        david.backward(5)
        
    else:
        print("FLAT")