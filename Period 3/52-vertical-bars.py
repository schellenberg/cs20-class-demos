import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

                       # R   G  B
blue_pixel = image.Pixel(0, 0, 255)
red_pixel = image.Pixel(255, 0, 0)

for y in range(height):
    for x in range(width):
        if x % 4 == 0:
            the_image.set_pixel(x, y, red_pixel)

    the_image.draw(canvas)


