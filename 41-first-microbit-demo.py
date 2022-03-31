import microbit
import time

#microbit.display.scroll("Hello, CS20!")

for letter in ["W", "M", "C", "I"]:
    microbit.display.show(letter)
    time.sleep(0.5)
