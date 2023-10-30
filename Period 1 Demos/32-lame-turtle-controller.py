import microbit
import turtle

window = turtle.Screen()
katos = turtle.Turtle()

while True:
    x = microbit.accelerometer.get_x()
    if x > 300:
        print("Tilted RIGHT!")
        katos.forward(5)
    elif x < -300:
        print("Tilted LEFT!")
        katos.backward(5)