import turtle

def draw_instructions(some_turtle, instructions, length, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(length)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

def apply_rules(letter):
    '''Applies the rules to a single letter and returns it.'''
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter
    
def process_string(some_string):
    '''Apply the rules to each letter in a string, and return the result.'''
    next_string = ""
    for letter in some_string:
        next_string = next_string + apply_rules(letter)
    return next_string

def create_l_system(iterations, axiom):
    '''Start with the axiom, then apply the rules iteration times.'''
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string


canvas = turtle.Screen()
joel = turtle.Turtle()
joel.shape("turtle")
joel.speed(0)

joel.penup()
joel.goto(-300, -300)
joel.pendown()

axiom = "FXF--FF--FF"
shape = create_l_system(6, axiom)
print(len(shape))
draw_instructions(joel, shape, 5, 60)

