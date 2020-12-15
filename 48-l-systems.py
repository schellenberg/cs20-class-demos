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
    # rule 1
    if letter == "F":
        return "FF"
    
    # rule 2
    elif letter == "X":
        return "--FXF++FXF++FXF--"

    # if no rules apply, just keep the same letter
    else:
        return letter

def process_string(original_string):
    new_string = ""
    for letter in original_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, depth):
    new_string = axiom
    for counter in range(depth):
        new_string = process_string(new_string)
    return new_string


window = turtle.Screen()
mitchell = turtle.Turtle()
mitchell.pensize(2)
mitchell.speed(0)

#goto bottom left
mitchell.penup()
mitchell.goto(-700, -475)
mitchell.pendown()

instructions = create_l_system("FXF--FF--FF", 6)
draw_instructions(mitchell, instructions, 10, 60)
