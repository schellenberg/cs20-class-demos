import turtle

def get_location(x, y):
    print(f"You clicked at x: {x}, y: {y}")

canvas = turtle.Screen()

canvas.onscreenclick(get_location)