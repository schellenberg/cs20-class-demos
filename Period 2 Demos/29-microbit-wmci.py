import microbit
import time

#microbit.display.scroll("Computer Science!")

# microbit.display.show("W")
# time.sleep(0.5)
# microbit.display.show("M")
# time.sleep(0.5)
# microbit.display.show("C")
# time.sleep(0.5)
# microbit.display.show("I")


for letter in ["W", "M", "C", "I"]:
    microbit.display.show(letter)
    time.sleep(0.5)
