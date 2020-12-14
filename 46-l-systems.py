import turtle

def apply_rules(letter):
    #rule 1
    if letter == "F":
        return "FF"
    
    #rule 2
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    
    #doesn't fit a rule
    return letter

def process_string(original_string):
    transformed_string = ""
    for letter in original_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(depth, axiom):
    instructions = axiom
    for counter in range(depth):
        instructions = process_string(instructions)
    return instructions

def draw_l_system(some_turtle, instructions, length, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(length)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)



canvas = turtle.Screen()
kyran = turtle.Turtle()
kyran.speed(0)
kyran.pensize(2)

#send turtle to bottom left
kyran.penup()
kyran.goto(-750, -500)
kyran.pendown()

instructions = create_l_system(6, "FXF--FF--FF")
draw_l_system(kyran, instructions, 5, 60)


