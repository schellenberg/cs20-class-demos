import microbit
import time

#microbit.display.scroll("Good morning, CS20!")

# microbit.display.show("W")
# time.sleep(1)
# microbit.display.show("M")
# time.sleep(1)
# microbit.display.show("C")
# time.sleep(1)
# microbit.display.show("I")

for letter in ["W", "M", "C", "I"]:
    microbit.display.show(letter)
    time.sleep(1)
