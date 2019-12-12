import microbit

press_count = 0

while True:
    if microbit.button_a.was_pressed():
        press_count += 1
        print(press_count)
        microbit.display.show(press_count)
    
    elif microbit.button_b.was_pressed():
        press_count = 0
        microbit.display.clear()