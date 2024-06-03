import turtle

def draw_string(some_turtle, instructions, distance, angle):
    '''Use some_turtle to draw each step in the instructions,
       moving by distance, and turning by angle.'''
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)

def apply_rules(letter):
    '''Apply rules to a specific letter, and return the result.'''
    if letter == "F":
        return "FF"
    
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    
    else:
        return letter
    
def process_string(some_string):
    '''Applies the rules to each letter in a string, then
       returns the result.'''
    new_string = ""
    for letter in some_string:
        new_string = new_string + apply_rules(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    '''Start with the axiom, process the string number_of_iterations
       times, then return the result.'''
    new_string = axiom
    for counter in range(number_of_iterations):
        new_string = process_string(new_string)
    return new_string


canvas = turtle.Screen()
riley = turtle.Turtle()
riley.speed(0)

#go to bottom right
riley.penup()
riley.goto(-300, -350)
riley.pendown()

instructions = create_l_system("FXF--FF--FF", 6)
draw_string(riley, instructions, 4, 60)

        
        