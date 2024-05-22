#red rectangle

import image

width = 250
height = 200

window = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

red_pixel = image.Pixel(255, 0, 0)
#to look at every pixel, use a nested for loop!
for y in range(height):
    for x in range(width):
        img.set_pixel(x, y, red_pixel)

    img.draw(window)