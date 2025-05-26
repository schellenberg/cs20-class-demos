import turtle

def draw_string(some_turtle, shape, length, angle):
    '''Draws the shape using some_turtle.
       F: forward
       -: left
       +: right'''
    for letter in shape:
        if letter == "F":
            some_turtle.forward(length)
        elif letter == "+":
            some_turtle.right(angle)
        elif letter == "-":
            some_turtle.left(angle)

def apply_rules(letter):
    '''Apply the rules to a letter and return the result.'''
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "--FXF++FXF++FXF--"
    else:
        return letter

def process_string(some_string):
    '''Apply the rules to every letter in the string, and return the result.'''
    result = ""
    for letter in some_string:
        result = result + apply_rules(letter)
    return result

def create_l_system(iterations, axiom):
    '''Start with the axiom and apply the rules iterations times.'''
    result = axiom
    for counter in range(iterations):
        result = process_string(result)
    return result


canvas = turtle.Screen()
aidan = turtle.Turtle()
aidan.shape("turtle")

aidan.speed(0)
aidan.penup()
aidan.goto(-300, -300)
aidan.pendown()

axiom = "FXF--FF--FF"
shape = create_l_system(7, axiom)
print(len(shape))
draw_string(aidan, shape, 2, 60)
