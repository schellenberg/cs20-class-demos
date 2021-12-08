import turtle

window = turtle.Screen()
joel = turtle.Turtle()

def draw_square(my_turtle, side_length):
    for side in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

def draw_square_from_center(a_turtle, side_length):
    #go to bottom left
    a_turtle.penup()
    a_turtle.right(90)
    a_turtle.forward(side_length/2)
    a_turtle.right(90)
    a_turtle.forward(side_length/2)
    a_turtle.right(180)
    a_turtle.pendown()
    
    #draw square
    draw_square(a_turtle, side_length)
    
    #go back to start/middle
    a_turtle.penup()
    a_turtle.forward(side_length/2)
    a_turtle.left(90)
    a_turtle.forward(side_length/2)
    a_turtle.right(90)
    a_turtle.pendown()

#inner squares
# draw_square_from_center(joel, 100)
# draw_square_from_center(joel, 150)

#square logo
draw_square_from_center(joel, 200)
joel.left(45)
draw_square_from_center(joel, 200)

#overlapped squares
# draw_square_from_center(joel, 200)
# draw_square(joel, 200)

