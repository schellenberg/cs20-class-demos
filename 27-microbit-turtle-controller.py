import turtle
import microbit

window = turtle.Screen()
laura = turtle.Turtle()
laura.color("blue")
laura.shape("turtle")

while True:
    x = microbit.accelerometer.get_x()
    print(x)

    if x > 300:
        print("RIGHT!")
        laura.forward(5)
        
    elif x < -300:
        print("LEFT!")
        laura.backward(5)