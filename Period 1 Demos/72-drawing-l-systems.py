import turtle

def apply_rules(letter):
    '''Return the changed string, based on the rules.'''
    #rule 1
    if letter == "A":
        return "B"
    
    #rule 2
    elif letter == "B":
        return "AB"
    
    #if it's not one of the rules, just send it back
    else:
        return letter
    
def process_string(instructions):
    '''Apply the rules to every letter in the instructions string.'''
    new_string = ""
    for letter in instructions:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(number_of_iterations, axiom):
    '''Start with the axiom, then apply the rules number_of_iterations times.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string

def draw_l_system(some_turtle, instructions, angle, distance):
    '''Draw the instructions with some_turtle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)


canvas = turtle.Screen()
justin = turtle.Turtle()

instructions = "FF++F++FF++F"
draw_l_system(justin, instructions, 45, 50)
