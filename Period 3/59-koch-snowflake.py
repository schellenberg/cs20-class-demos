import turtle

def apply_rules(letter):
    '''Apply the rules to a single letter.'''
    if letter == "F":
        return "F-F++F-F"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(the_string):
    '''Apply the rules to each letter in the_string.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_L_system(axiom, iterations):
    '''Start with the axiom, then apply the rules iterations times.'''
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string

def draw_instructions(some_turtle, instructions, distance, angle):
    '''Draw each instruction with some_turtle, moving forward by
       distance, and turning by angle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

canvas = turtle.Screen()
charlie = turtle.Turtle()
charlie.speed(0)

charlie.penup()
charlie.goto(-600, -400)
charlie.pendown()

instructions = create_L_system("F", 4)
draw_instructions(charlie, instructions, 10, 60)