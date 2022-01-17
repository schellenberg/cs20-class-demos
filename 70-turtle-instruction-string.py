import turtle

canvas = turtle.Screen()
eason = turtle.Turtle()

def draw_l_system(a_turtle, instructions, angle, distance):
    for task in instructions:
        if task == "F":
            a_turtle.forward(distance)
        elif task == "+":
            a_turtle.right(angle)
        elif task == "-":
            a_turtle.left(angle)

def apply_rules(letter):
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter
    
def apply_rules_to_string(the_string):
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(iterations, axiom):
    new_string = axiom
    for number in range(iterations):
        new_string = apply_rules_to_string(new_string)
    return new_string


#send eason to bottom left
eason.speed(0)
eason.penup()
eason.goto(-500, -400)
eason.pendown()

instructions = create_l_system(6, "FXF--FF--FF")
draw_l_system(eason, instructions, 60, 5)
print(instructions)
print(len(instructions))