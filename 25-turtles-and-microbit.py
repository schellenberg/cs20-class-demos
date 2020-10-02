import microbit
import time
import turtle

while True:
    x = microbit.accelerometer.get_x()
    print(x)
    
    time.sleep(0.5)
