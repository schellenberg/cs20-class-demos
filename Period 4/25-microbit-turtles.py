import microbit
import turtle

window = turtle.Screen()
sathini = turtle.Turtle()
sathini.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
#     print(x)

    if x > 200:
        print("RIGHT")
        sathini.forward(2)
        
    elif x < -200:
        print("LEFT")
        sathini.backward(2)
        
    else:
        print("FLAT")
