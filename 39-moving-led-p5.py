import microbit

def make_image(led_x):
    upper_part = "00000:" \
                 "00000:" \
                 "00000:" \
                 "00000:"

    possible_bottoms = ["70000", "07000", "00700", "00070", "00007"]
    led_grid = upper_part + possible_bottoms[led_x]

    screen = microbit.Image(led_grid)
    return screen
    

x = 2
current_image = make_image(x)
microbit.display.show(current_image)

while True:
    if microbit.button_a.is_pressed():
        x = x - 1
        if x < 0:
            x = 4
        current_image = make_image(x)
        microbit.display.show(current_image)
    
    if microbit.button_b.is_pressed():
        x = x + 1
        if x > 4:
            x = 0
        current_image = make_image(x)
        microbit.display.show(current_image)