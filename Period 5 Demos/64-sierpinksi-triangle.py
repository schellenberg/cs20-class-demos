import turtle

def apply_rules(letter):
    '''Apply rule to a single letter and return the result.'''
    #rule 1
    if letter == "F":
        return "FF"
    
    #rule 2
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    
    #not a rule, so just send it back unchanged
    else:
        return letter
    
def process_string(the_string):
    '''Apply the rules to every letter in an entire string, and return it.'''
    new_string = ""
    for letter in the_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    '''Start with the axiom, then apply the rules number_of_iterations times.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string 

def draw_instructions(some_turtle, instructions, angle, distance):
    '''Draw a shape based on the instructions given.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

window = turtle.Screen()
evan = turtle.Turtle()
evan.speed(0)

evan.penup()
evan.goto(-600, -400)
evan.pendown()

instructions = create_l_system("FXF--FF--FF", 7)
draw_instructions(evan, instructions, 60, 3)
window.exitonclick()
