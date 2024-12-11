import image

width = 500
height = 300

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

                       # R   G  B
red_pixel = image.Pixel(255, 0, 0)
blue_pixel = image.Pixel(0, 0, 255)

for x in range(width):
    the_image.set_pixel(x, 50, red_pixel)

for y in range(height):
    the_image.set_pixel(400, y, blue_pixel)

the_image.draw(canvas)