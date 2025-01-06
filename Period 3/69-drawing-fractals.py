import turtle

def apply_rules(letter):
    '''Apply the rules to a letter, and return the result.'''
    if letter == "F":
        return "F-F++F-F"
    elif letter == "B":
        return "AB"
    else:
        return letter

def process_string(the_string):
    '''Apply the rules to each letter in a string, and
       return the result.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, iterations):
    '''Start with the axiom, then apply the rules to string
       number of iterations times. Return the result.'''
    the_string = axiom
    for counter in range(iterations):
        the_string = process_string(the_string)
    return the_string

def draw_l_system(some_turtle, instructions, angle, distance):
    '''Draw the instructions with some_turtle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

window = turtle.Screen()
khoi = turtle.Turtle()
khoi.speed(0)

#move to bottom left
khoi.penup()
khoi.goto(-300, -300)
khoi.pendown()

tasks = create_l_system("F", 4)
draw_l_system(khoi, tasks, 60, 10)
        