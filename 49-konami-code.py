import microbit

actions = []
current_action = ""

def get_konami_action(sensitivity_amount):
    """Returns a single action that has occured on the Micro:bit, either a button a or b, then a tilt
    value of right, left, up or down. The sensitivity_amount affects all the tilt options."""
    x_tilt = microbit.accelerometer.get_x()
    y_tilt = microbit.accelerometer.get_y()

    if microbit.button_a.was_pressed():
        return "a"

    elif microbit.button_b.was_pressed():
        return "b"

    # if tilted more on one axis, use that axis to determine the 'direction' of the tilt
    elif abs(x_tilt) > abs(y_tilt):
        # use x axis
        if x_tilt > sensitivity_amount:
            return "right"

        elif x_tilt < -1 * sensitivity_amount:
            return "left"

    else:
        # use y axis
        if y_tilt > sensitivity_amount:
            return "down"

        elif y_tilt < -1 * sensitivity_amount:
            return "up"

def konami_code(action_list):
    """Look for the pattern up, up, down, down, left, left, right, right, b, a at the end of a list.
    Return True if the pattern is found, False if it is not."""

    if len(action_list) < 10:
        return False
    else:
        return (action_list[-1] == "a" and action_list[-2] == "b" and
                action_list[-3] == "right" and action_list[-4] == "left" and
                action_list[-5] == "right" and action_list[-6] == "left" and
                action_list[-7] == "down" and action_list[-8] == "down" and
                action_list[-9] == "up" and action_list[-10] == "up")



while True:
    # remember what the action was last time through the loop
    last_action = current_action
    current_action = get_konami_action(700)

    # is this a "new" action?
    if current_action != last_action and current_action != None:
        actions.append(current_action)
        print(actions)

    if konami_code(actions):
        break

print("Easter egg time!!!")