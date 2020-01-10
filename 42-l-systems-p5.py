import turtle

canvas = turtle.Screen()
anna = turtle.Turtle()
saved_locations = []

def draw_string(instructions, some_turtle, distance, angle):
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
            saved_locations.append([x, y, heading])
        if task == "]":
            some_turtle.penup()
            new_location = saved_locations.pop()
            some_turtle.goto(new_location[0], new_location[1])
            some_turtle.setheading(new_location[2])
            some_turtle.pendown()

def apply_rules(some_letter):
    if some_letter == "X":
        return "F[-X]+X"
    elif some_letter == "F":
        return "FF"
    else:
        return some_letter

def process_string(original_string):
    converted_string = ""
    for letter in original_string:
        converted_string = converted_string + apply_rules(letter)
    return converted_string

def create_l_system(axiom, level):
    converted_string = axiom
    for counter in range(level):
        converted_string = process_string(converted_string)
    return converted_string

#move turtle to bottom left
# anna.speed(0)

anna.penup()
anna.goto(0, -400)
anna.left(90)
anna.pendown()
anna.pensize(2)

#canvas.tracer(2)

instructions = create_l_system("X", 6)
# print(instructions)
draw_string(instructions, anna, 5, 30)