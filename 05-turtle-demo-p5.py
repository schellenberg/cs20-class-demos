import turtle

window = turtle.Screen()

anna = turtle.Turtle()
anna.shape("turtle")
anna.color("red")
anna.speed(0)

for shape in range(36):
    for side in range(6):
        anna.forward(200)
        anna.left(360/6)
    anna.left(10)