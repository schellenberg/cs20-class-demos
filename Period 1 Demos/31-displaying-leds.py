import microbit
import time

#microbit.display.scroll("Good morning, CS20!")

for letter in ["W", "M", "C"]:
    microbit.display.show(letter)
    time.sleep(0.5)

