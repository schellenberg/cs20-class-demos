import turtle

def print_coordinates(x, y):
    location_message = f"x: {x},    y: {y}"
    print(location_message)

canvas = turtle.Screen()

amy = turtle.Turtle()
amy.shape("turtle")
amy.pensize(5)

canvas.onclick(print_coordinates)
