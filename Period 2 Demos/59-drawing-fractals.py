import turtle

def apply_rules(letter):
    #rule 1
    if letter == "F":
        return "FF"
    
    #rule 2
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    
    #no rules apply
    else:
        return letter
    
def transform_string(some_string):
    new_string = ""
    for letter in some_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    the_string = axiom
    for counter in range(number_of_iterations):
        the_string = transform_string(the_string)
    return the_string

def draw_l_system(some_turtle, instructions, angle, distance):
    for item in instructions:
        if item == "F":
            some_turtle.forward(distance)
        elif item == "+":
            some_turtle.right(angle)
        elif item == "-":
            some_turtle.left(angle)

canvas = turtle.Screen()
faith = turtle.Turtle()
faith.speed(0)

#go to bottom left of screen
faith.penup()
faith.goto(-250, -250)
faith.pendown()

task = create_l_system("FXF--FF--FF", 6)
draw_l_system(faith, task, 60, 5)

