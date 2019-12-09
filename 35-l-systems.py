import turtle

window = turtle.Screen()
amy = turtle.Turtle()

def draw_the_string(instructions, some_turtle, distance, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        if task == "-":
            some_turtle.left(angle)
        if task == "+":
            some_turtle.right(angle)

def apply_rules(letter):
    if letter == "F":
        return "F-F++F-F"
#     elif letter == "B":
#         return "AB"
    else:
        return letter

def process_string(some_string):
    transformed_string = ""
    for letter in some_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string

def create_l_system(axiom, level):
    transformed_string = axiom
    for counter in range(level):
        transformed_string = process_string(transformed_string)
    return transformed_string

# print(create_l_system("A", 5))

# move to bottom left of screen
amy.penup()
amy.goto(-600, -400)
amy.pendown()

amy.speed(0)
window.tracer(2)

instructions = create_l_system("F", 5)
draw_the_string(instructions, amy, 5, 60)