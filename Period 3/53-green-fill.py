import image

width = 400
height = 200

window = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

                         #R   G   B
green_pixel = image.Pixel(0, 255, 0)

for y in range(height):
    for x in range(width):
        the_image.set_pixel(x, y, green_pixel)

    the_image.draw(window)