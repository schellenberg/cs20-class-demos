import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

blue_pixel = image.Pixel(0, 0, 255)
red_pixel = image.Pixel(255, 0, 0)
for y in range(height):
    for x in range(width):
        if x % 2 == 0:
            img.set_pixel(x, y, blue_pixel)
        else:
            img.set_pixel(x, y, red_pixel)

img.draw(canvas)