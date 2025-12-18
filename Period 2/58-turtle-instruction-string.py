import turtle

def draw_instructions(instructions, some_turtle, step_size, angle):
    for task in instructions:
        if task == "F":
            some_turtle.forward(step_size)
        elif task == "-":
            some_turtle.left(angle)
        elif task == "+":
            some_turtle.right(angle)
            
            
canvas = turtle.Screen()
somaya = turtle.Turtle()

instructions = "F++FF++F++FF"
draw_instructions(instructions, somaya, 150, 45)
