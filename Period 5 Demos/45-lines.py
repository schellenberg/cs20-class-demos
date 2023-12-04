import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

the_pixel = image.Pixel(0, 0, 255)
for x in range(width):
    the_image.set_pixel(x, 200, the_pixel)

other_pixel = image.Pixel(255, 0, 0)
for y in range(height):
    the_image.set_pixel(300, y, other_pixel)

the_image.draw(canvas)