import turtle

canvas = turtle.Screen()

chris = turtle.Turtle()
chris.pensize(4)
#chris.speed(1)

def draw_rectangle(some_turtle, length, width):
    for counter in range(2):
        some_turtle.forward(width)
        some_turtle.left(90)
        some_turtle.forward(length)
        some_turtle.left(90)
        
for rectangle in range(8):
    draw_rectangle(chris, 200, 75)
    chris.forward(75)
    chris.right(360/8)
    
