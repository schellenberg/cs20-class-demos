import image

width = 300
height = 150

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

red_pixel = image.Pixel(255, 0, 0)
for x in range(width):
    the_image.set_pixel(x, 75, red_pixel)

blue_pixel = image.Pixel(0, 0, 255)
for y in range(height):
    the_image.set_pixel(250, y, blue_pixel)

the_image.draw(canvas)