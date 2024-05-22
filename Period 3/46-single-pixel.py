import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

                        # R   G  B
this_pixel = image.Pixel(255, 0, 0)
for x in range(width):
    the_image.set_pixel(x, 150, this_pixel)

                        # R   G  B
green_pixel = image.Pixel(0, 255, 0)
for y in range(height):
    the_image.set_pixel(320, y, green_pixel)

the_image.draw(canvas)