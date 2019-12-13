import microbit

def make_image(led_location):
    upper_grid = "00000:" \
                 "00000:" \
                 "00000:" \
                 "00000:"
    bottom_row_options = ["70000", "07000", "00700", "00070", "00007"]

    led_grid = upper_grid + bottom_row_options[led_location]
    screen = microbit.Image(led_grid)
    return screen

x = 2
current_image = make_image(x)
microbit.display.show(current_image)

while True:
    if microbit.button_a.was_pressed():
        x = x - 1
        if x < 0:
            x = 4
        current_image = make_image(x)
        microbit.display.show(current_image)
    
    elif microbit.button_b.was_pressed():
        x = x + 1
        if x > 4:
            x = 0
        current_image = make_image(x)
        microbit.display.show(current_image)