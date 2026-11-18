import turtle

def draw_square(a_turtle, side_length):
    '''Draws a square with a_turtle, where each side is side_length long.'''
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)

def draw_centered_square(some_turtle, side_length):
    '''Draw a square with sides of side_length long. Start and end
       in the exact center of the square.'''
    #moved to bottom left of the square
    some_turtle.penup()
    some_turtle.backward(side_length/2)
    some_turtle.right(90)
    some_turtle.forward(side_length/2)
    some_turtle.left(90)
    some_turtle.pendown()
    
    draw_square(some_turtle, side_length)
    
    #move back to center of square
    some_turtle.penup()
    some_turtle.left(90)
    some_turtle.forward(side_length/2)
    some_turtle.right(90)
    some_turtle.forward(side_length/2)
    some_turtle.pendown()

window = turtle.Screen()
window.bgcolor("lightgreen")

himal = turtle.Turtle()
himal.color("blue")
himal.pensize(4)

#inner squares
# draw_centered_square(himal, 300)
# draw_centered_square(himal, 200)

#square logo
# draw_centered_square(himal, 300)
# himal.left(45)
# draw_centered_square(himal, 300)

#overlapping squares
draw_square(himal, 300)
draw_centered_square(himal, 300)