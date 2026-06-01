import turtle

def draw_instructions(instructions, some_turtle, distance, angle):
    '''Draw each of the instructions with some_turtle. Use distance
       to move forward, and turn by the given angle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

def apply_rules(letter):
    '''Apply the rules to an individual letter.'''
    if letter == "F":
        return "F-F++F-F"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(the_string):
    '''Apply the rules to the_string, one letter at a time.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_L_system(iterations, axiom):
    '''Start with the axiom, and apply the rules iterations times.'''
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string

canvas = turtle.Screen()
kabeer = turtle.Turtle()
kabeer.speed(0)

#go to bottom left
kabeer.penup()
kabeer.goto(-800, -500)
kabeer.pendown()

instructions = create_L_system(4, "F")
draw_instructions(instructions, kabeer, 10, 60)