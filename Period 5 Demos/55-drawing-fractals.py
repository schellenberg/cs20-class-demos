import turtle

def change_character(letter):
    #rule 1
    if letter == "F":
        return "FF"
    
    #rule 2
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    
    #catch all
    else:
        return letter
    
def convert_string(some_string):
    new_string = ""
    for letter in some_string:
        new_string = new_string + change_character(letter)
    return new_string

def create_l_system(axiom, number_of_iterations):
    l_system = axiom
    for counter in range(number_of_iterations):
        l_system = convert_string(l_system)
    return l_system

def draw_l_system(some_turtle, instructions, angle, distance):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)
    

window = turtle.Screen()
jessica = turtle.Turtle()
jessica.speed(0)

#go to bottom left
jessica.penup()
jessica.goto(-250, -250)
jessica.pendown()

instructions = create_l_system("FXF--FF--FF", 6)
draw_l_system(jessica, instructions, 60, 5)
