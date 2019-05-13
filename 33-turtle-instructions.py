import turtle

def apply_rules(letter):
    #rule 1
    if letter == "F":
        new_string = "F-F++F-F"
    
    #rule 2
#    elif letter == "B":
#        new_string = "AB"
    
    else:
        new_string = letter
    
    return new_string

def process_string(original_string):
    transformed_string = ""
    for letter in original_string:
        transformed_string = transformed_string + apply_rules(letter)
    return transformed_string
    
def create_L_system(number_of_iterations, axiom):
    system_string = axiom
    for counter in range(number_of_iterations):
        system_string = process_string(system_string)
    return system_string

def draw_L_system(some_turtle, instructions, angle, distance):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "B":
            some_turtle.backward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

########################################################

window = turtle.Screen()
mark = turtle.Turtle()

mark.speed(0)

mark.up()
mark.back(250)
mark.down()

instructions = create_L_system(2, "F")
draw_L_system(mark, instructions, 60, 50)
