import turtle

canvas = turtle.Screen()
haris = turtle.Turtle()
haris.speed(0)

def draw_l_system(some_turtle, instructions, angle, distance):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

def apply_rules(letter):
    #Rule 1
    if letter == "F":
        return "F-F++F-F"
    
    #Rule 2
    #elif letter == "B":
    #    return "AB"
    
    #no rules apply, so keep the letter as is
    else:
        return letter

def process_string(original_string):
    transformed_string = ""
    for letter in original_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(iterations, axiom):
    the_string = axiom
    for counter in range(iterations):
        the_string = process_string(the_string)
    return the_string

#move haris to the bottom left
haris.penup()
haris.goto(-600, -450)
haris.pendown()

instructions = create_l_system(5, "F")
draw_l_system(haris, instructions, 60, 5)