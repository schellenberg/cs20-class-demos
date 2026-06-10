import turtle

def draw_cross(some_turtle, side_length):
        """Simplest way. Used in drag/drop demo."""
        # repeat the same shape four times so the turtle returns to the starting orientation
        for tower in range(4):
            # draw three sides of a square, then turn to make the cross shape
            for side in range(3):
                some_turtle.forward(side_length)
                some_turtle.left(90)
            some_turtle.left(180)
            
def draw_cross_from_bottom_left(some_turtle, side_length):
        """Used in second and third questions, though many other ways possible too. Draws a cross shape with the given some_turtle, with each side being side_length long."""
        for l_shape in range(4):
            for angle in [90, -90, 90]:
                some_turtle.forward(side_length)
                some_turtle.left(angle)

def draw_second_shape(some_turtle, side_length):
    '''Draws a shape made out of four crosses.'''
    for cross in range(4):
        draw_cross_from_bottom_left(some_turtle, side_length)
        # after each cross, turn 90 degrees so the next one is drawn in a new direction
        some_turtle.left(90)

def draw_third_shape(some_turtle, side_length):
    '''Draws a shape made out of eight crosses. Four are the same as the second shape, and the other four are rotated 45 degrees.'''
    draw_second_shape(some_turtle, side_length)
    # rotate halfway between the first set of crosses and draw the same pattern again
    some_turtle.left(45)
    draw_second_shape(some_turtle, side_length)

# create the drawing window and the turtle
canvas = turtle.Screen()
emily = turtle.Turtle()
emily.speed(0)

# draw_cross(emily, 50)
draw_third_shape(emily, 50)