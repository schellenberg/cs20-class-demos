import microbit

def is_tilted_left(sensitivity):
    x_tilt = microbit.accelerometer.get_x()
    return x_tilt < -1 * sensitivity

def is_tilted_right(sensitivity):
    x_tilt = microbit.accelerometer.get_x()
    return x_tilt > sensitivity

def is_tilted_down(sensitivity):
    y_tilt = microbit.accelerometer.get_y()
    return y_tilt < -1 * sensitivity

def is_tilted_up(sensitivity):
    y_tilt = microbit.accelerometer.get_y()
    return y_tilt > sensitivity

while True:
    if is_tilted_left(300):
        print("LEFT")
        microbit.display.show("L")
    elif is_tilted_right(300):
        print("RIGHT")
        microbit.display.show("R")
        
    elif is_tilted_up(300):
        print("UP")
        microbit.display.show("U")
    elif is_tilted_down(300):
        print("DOWN")
        microbit.display.show("D")