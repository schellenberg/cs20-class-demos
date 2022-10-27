import turtle

#setting up the screen and turtle
window = turtle.Screen()
jayden = turtle.Turtle()
jayden.shape("turtle")

#draw a shape
# counter = 0
# while counter < 4:
#     jayden.forward(100)
#     jayden.left(90)
#     counter = counter + 1

for side in range(4):
    jayden.forward(100)
    jayden.left(90)