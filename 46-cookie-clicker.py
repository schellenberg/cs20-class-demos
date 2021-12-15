import microbit

cookies = 0

while True:
    if microbit.button_a.was_pressed():
        cookies += 1
        print(cookies)
    
    elif microbit.button_b.was_pressed():
        cookies = 0