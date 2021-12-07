import turtle

def draw_square(a_turtle, side_length):
    """Use a_turtle to draw a square of side_length sides."""
    for side in range(4):
        a_turtle.forward(side_length)
        a_turtle.left(90)
        
        
window = turtle.Screen()
michael = turtle.Turtle()
josh = turtle.Turtle()
josh.color("red")

draw_square(michael, 150)
draw_square(josh, 250)

window.exitonclick()