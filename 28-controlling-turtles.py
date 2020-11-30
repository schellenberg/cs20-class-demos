import microbit
import time
import turtle

window = turtle.Screen()
rylan = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()
    #print(x)
    
    if x > 200:
        print("Right")
        rylan.forward(5)
        
    elif x < -200:
        print("Left")
        rylan.backward(5)
        
    else:
        print("Flat")
        
    time.sleep(0.1)
