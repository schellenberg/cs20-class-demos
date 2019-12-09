import turtle

canvas = turtle.Screen()
anna = turtle.Turtle()

def draw_string(instructions, some_turtle, distance, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        if task == "-":
            some_turtle.left(angle)
        if task == "+":
            some_turtle.right(angle)

def apply_rules(some_letter):
    if some_letter == "L":
        return "+R-F-R+"
    elif some_letter == "R":
        return "-L+F+L-"
    else:
        return some_letter

def process_string(original_string):
    converted_string = ""
    for letter in original_string:
        converted_string = converted_string + apply_rules(letter)
    return converted_string

def create_l_system(axiom, level):
    converted_string = axiom
    for counter in range(level):
        converted_string = process_string(converted_string)
    return converted_string

#move turtle to bottom left
anna.speed(0)

anna.penup()
anna.goto(-600, 0)
anna.pendown()
anna.pensize(2)

canvas.tracer(2)

instructions = create_l_system("L--F--L--F", 8)
# print(instructions)
draw_string(instructions, anna, 20, 45)