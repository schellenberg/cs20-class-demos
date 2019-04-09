import turtle

def where_is_this(x, y):
    print("x: " + str(x) + "  y:" + str(y))
    

canvas = turtle.Screen()

anu = turtle.Turtle()

canvas.onclick(where_is_this)
canvas.listen()