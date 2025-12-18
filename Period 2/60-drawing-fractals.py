import turtle

def apply_rules(letter):
    '''Apply rules to one letter, and return result.'''
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter
    
def process_string(the_string):
    '''Apply rules to every letter in a string, and return the result.'''
    transformed_string = ""
    for letter in the_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(number_of_iterations, axiom):
    '''Start with the axiom, then apply the rules number_of_iterations
       times. Return the result.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string

def draw_instructions(instructions, some_turtle, step_size, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(step_size)
        elif task == "-":
            some_turtle.left(angle)
        elif task == "+":
            some_turtle.right(angle)
            
            
canvas = turtle.Screen()
somaya = turtle.Turtle()

somaya.speed(0)
somaya.penup()
somaya.goto(-700, -500)
somaya.pendown()
somaya.pensize(2)

instructions = create_l_system(6, "FXF--FF--FF")
draw_instructions(instructions, somaya, 10, 60)

