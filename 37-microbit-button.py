import microbit

count = 0

while True:
    if microbit.button_a.was_pressed():
        count += 1
        print(count)
        microbit.display.show(count)
        
    elif microbit.button_b.was_pressed():
        count = 0
        print(count)
        microbit.display.show(count)