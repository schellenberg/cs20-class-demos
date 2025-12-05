import image

width = 200
height = 200

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

blue_pixel = image.Pixel(0, 0, 255)
for y in range(height):
    for x in range(width):
        the_image.set_pixel(x, y, blue_pixel)

    the_image.draw(canvas)
