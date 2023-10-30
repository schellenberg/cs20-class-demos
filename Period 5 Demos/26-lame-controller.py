import microbit
import turtle

canvas = turtle.Screen()
bennett = turtle.Turtle()

while True:
    tilt_x = microbit.accelerometer.get_x()
    
    if tilt_x > 400:
        print("Tilted RIGHT!")
        bennett.forward(5)
        
    elif tilt_x < -400:
        print("Tilted LEFT!")
        bennett.backward(5)
        
    else:
        print("Flat")