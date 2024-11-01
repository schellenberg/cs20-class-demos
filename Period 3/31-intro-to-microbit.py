import microbit
import time

# microbit.display.scroll("Hey there CS20!")

# microbit.display.show("W")
# time.sleep(1)
# microbit.display.show("M")
# time.sleep(1)
# microbit.display.show("C")


for letter in ["W", "M", "C"]:
    microbit.display.show(letter)
    time.sleep(1)
    
    