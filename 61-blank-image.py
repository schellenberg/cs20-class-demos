import image
import random

width = 400
height = 300

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

for x in range(width):
    red = random.randrange(255)
    blue = random.randrange(255)
    green = random.randrange(255)

    p = image.Pixel(red, blue, green)
    for y in range(height):
        img.set_pixel(x, y, p)

    img.draw(canvas)