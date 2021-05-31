import microbit
import turtle

window = turtle.Screen()
monica = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()
    
    if x > 300:
        print("Tilted to the right!")
        microbit.display.show("R")
        monica.forward(5)
    elif x < -300:
        print("Tilted to the left!")
        microbit.display.show("L")
        monica.backward(5)
    else:
        print("Not tilted")
        microbit.display.show("-")
    
    #print(x)