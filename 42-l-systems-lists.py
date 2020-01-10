import turtle

window = turtle.Screen()
amy = turtle.Turtle()
states = []

def draw_the_string(instructions, some_turtle, distance, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(distance)
        if task == "-":
            some_turtle.left(angle)
        if task == "+":
            some_turtle.right(angle)
        if task == "[":
            x = some_turtle.xcor()
            y = some_turtle.ycor()
            heading = some_turtle.heading()
            states.append([x, y, heading])
        if task == "]":
            new_location = states.pop()
            x = new_location[0]
            y = new_location[1]
            heading = new_location[2]
            some_turtle.penup()
            some_turtle.goto(x, y)
            some_turtle.setheading(heading)
            some_turtle.pendown()

def apply_rules(letter):
    if letter == "F":
        return "FF"
    elif letter == "X":
        return "F[-X]+X"
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
amy.goto(0, -400)
amy.left(90)
amy.pendown()

amy.speed(0)
#window.tracer(2)

instructions = create_l_system("X", 8)
draw_the_string(instructions, amy, 2, 30)
