import image

def check_odd(number):
    if number % 2 == 0:
        return False
    else:
        return True

width = 200
height = 300

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

some_pixel = image.Pixel(122, 0, 255)
for y in range(height):
    for x in range(width):
        if check_odd(x):
            img.set_pixel(x, y, some_pixel)

img.draw(canvas)
