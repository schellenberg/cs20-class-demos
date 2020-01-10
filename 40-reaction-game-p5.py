# Mico:bit Reaction Game
# Computer Science 20
# Dan Schellenberg

import microbit
import random
import time


def button_clicked(current_score, should_be_pressing):
    """Adds or subtracts from the current score, based on whether an image is showing."""
    if should_be_pressing == True:
        current_score = current_score + 1
    else:
        current_score = current_score - 2

    return current_score

def show_winner(a_score, b_score):
    """Print winner to console, and display winner on Micro:bit."""
    if a_score > b_score:
        print("Player A wins!")
        microbit.display.show("A")
    else:
        print("Player B wins!")
        microbit.display.show("B")

# global variables
a_score = 0
b_score = 0
someone_pressed_button = True
good_image = True
showing_image = False
time_to_wait = 0
starting_time = 0
ending_time = 0

# constants
POINTS_TO_WIN_GAME = 5


# game loop
while True:
    # check if need to pick a new amount of time to wait
    if someone_pressed_button == True:
        microbit.display.clear()
        showing_image = False

        # pausing execution for 0.5 seconds stops players from accidentally clicking more than once
        time.sleep(0.5)

        # show good or bad image
        image_choice = random.randrange(1, 3)
        if image_choice == 1:
            good_image = True
        else:
            good_image = False

        # determine when the image should reappear on the microbit        
        time_to_wait = random.randrange(1, 6)
        starting_time = time.time()  # unit is seconds

        someone_pressed_button = False

    # check if it is time to display the image
    time_now = time.time()
    time_since_start = time_now - starting_time

    # uncomment the following line to understand how the time works
    # print(time_since_start)

    # change the boolean to turn on the image if enough time has gone by
    if time_since_start > time_to_wait:
        showing_image = True

    # display image if enough time has elapsed
    if showing_image == True:
        if good_image:
            microbit.display.show(microbit.Image.HAPPY)
        else:
            microbit.display.show(microbit.Image.SAD)

    should_press = good_image and showing_image

    # deal with a button being pressed
    if microbit.button_a.is_pressed():
        a_score = button_clicked(a_score, should_press)
        print("Player A:", a_score, "    Player B:", b_score)
        someone_pressed_button = True

    if microbit.button_b.is_pressed():
        b_score = button_clicked(b_score, should_press)
        print("Player A:", a_score, "    Player B:", b_score)
        someone_pressed_button = True

    # if somebody wins, end the game
    if a_score >= POINTS_TO_WIN_GAME or b_score >= POINTS_TO_WIN_GAME:
        break

show_winner(a_score, b_score)
print("Game over!")