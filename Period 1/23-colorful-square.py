import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")

trey = turtle.Turtle()
trey.shape("turtle")
trey.color("red")
trey.pensize(10)

# #method 1 of making a square
# for side in [0, 1, 2, 3]:
#     trey.forward(100)
#     trey.left(90)
#     print(side)


# #method 2 of making a square
# for side in ["yusha", "ryan", 42, True]:
#     trey.forward(100)
#     trey.left(90)
#     print(side)


#method 3 of making a square
for some_color in ["red", "green", "blue", "yellow"]:
    trey.color(some_color)
    trey.forward(100)
    trey.left(90)
