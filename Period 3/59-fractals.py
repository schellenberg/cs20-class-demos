import turtle

def draw_string(some_turtle, intructions, distance, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

def apply_rules(letter):
    '''Apply the rules to a single letter, and return the result.'''
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter
    
def process_string(some_string):
    '''Apply the rules to every letter in a string, return the result.'''
    transformed_string = ""
    for letter in some_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(axiom, number_of_iterations):
    '''Start with the axiom, then apply the rules to the string
       number_of_iteration times, then return the result.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string


canvas = turtle.Screen()
utsho = turtle.Turtle()
utsho.speed(0)

#move to the bottom left
utsho.penup()
utsho.goto(-300, -350)
utsho.pendown()

instructions = create_l_system("FXF--FF--FF", 6)
draw_string(utsho, instructions, 3, 60)
    
    
    