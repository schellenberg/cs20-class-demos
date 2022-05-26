import turtle

def apply_rules(letter):
    if letter == "F":
        return "FF"
    
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    
    else:
        return letter

def process_string(the_string):
    transformed_string = ""
    for letter in the_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(axiom, how_many_levels):
    the_string = axiom
    for level in range(how_many_levels):
        the_string = process_string(the_string)
    return the_string

def draw_l_system(the_turtle, instructions, angle, distance):
    for task in instructions:
        if task == "F":
            the_turtle.forward(distance)
        elif task == "+":
            the_turtle.right(angle)
        elif task == "-":
            the_turtle.left(angle)


window = turtle.Screen()
ivy = turtle.Turtle()
ivy.speed(0)

ivy.penup()
ivy.goto(-250, -250)
ivy.pendown()


instructions = create_l_system("FXF--FF--FF", 7)
draw_l_system(ivy, instructions, 60, 2)
