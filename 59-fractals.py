import turtle


def apply_rules(letter):
    if letter == "F":
        return "FF"
    
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    
    else:
        return letter

def process_string(some_string):
    transformed_string = ""
    for letter in some_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(iterations, axiom):
    new_string = axiom
    for counter in range(iterations):
        new_string = process_string(new_string)
    return new_string

def draw_l_system(some_turtle, instructions, angle, distance):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)



window = turtle.Screen()
ayman = turtle.Turtle()
ayman.speed(0)
ayman.penup()
ayman.goto(-600, -400)
ayman.pendown()

instructions = create_l_system(6, "FXF--FF--FF")
draw_l_system(ayman, instructions, 60, 5)

