import turtle

def apply_rules(letter):
    if letter == "A":
        return "B"
    
    elif letter == "B":
        return "AB"
    
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

instructions = "F++F++F++F"
draw_l_system(ivy, instructions, 45, 50)
