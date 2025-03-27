import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

thy = turtle.Turtle()
thy.shape("turtle")
thy.color("green")
thy.pensize(5)

#different ways to draw a square
# method 1
# thy.forward(100)
# thy.left(90)
# thy.forward(100)
# thy.left(90)
# thy.forward(100)
# thy.left(90)
# thy.forward(100)
# thy.left(90)

# method 2 -- while loop
# counter = 0
# while counter < 4:
#     thy.forward(100)
#     thy.left(90)
#     counter = counter + 1

# method 3 -- for loop
# for side in range(4):
#     thy.forward(100)
#     thy.left(90)


# method 4 -- another for loop
# for side in [0, 1, 2, 3]:
#     thy.forward(100)
#     thy.left(90)


# method 5 -- yet another for loop
# for side in ["linden", "noor", 42, False]:
#     thy.forward(100)
#     thy.left(90)
#     print(side)
    

# method 6 -- yet one more for loop
for some_color in ["red", "blue", "green", "yellow"]:
    thy.color(some_color)
    thy.forward(100)
    thy.left(90)
    
    
    