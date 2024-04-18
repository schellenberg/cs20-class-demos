import microbit
import turtle

the_window = turtle.Screen()
dmitrii = turtle.Turtle()
dmitrii.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    
    if x > 250:
        print("RIGHT")
        dmitrii.forward(5)
        
    elif x < -250:
        print("LEFT")
        dmitrii.backward(5)
    
    else:
        print("FLAT")
