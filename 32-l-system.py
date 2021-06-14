import turtle

def apply_rules(letter):
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter
    
def process_string(instructions):
    new_instructions = ""
    for letter in instructions:
        new_instructions = new_instructions + apply_rules(letter)
    return new_instructions

def create_l_system(number_of_iterations, axiom):
    l_system = axiom
    for counter in range(number_of_iterations):
        l_system = process_string(l_system)
    return l_system

canvas = turtle.Screen()
canvas.bgcolor("lightgreen")

sebastian = turtle.Turtle()
sebastian.color("blue")
sebastian.shape("turtle")
sebastian.speed(0)
sebastian.penup()
sebastian.backward(250)
sebastian.pendown()

instructions = create_l_system(5, "FXF--FF--FF")
line_length = 10
angle = 60
print(instructions)

for task in instructions:
    if task == "F":
        sebastian.forward(line_length)
    elif task == "+":
        sebastian.right(angle)
    elif task == "-":
        sebastian.left(angle)
