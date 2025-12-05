import image

width = 400
height = 600

canvas = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

red_pixel = image.Pixel(255, 0, 0)
for x in range(width):
    the_image.set_pixel(x, 200, red_pixel)
    
green_pixel = image.Pixel(0, 255, 0)
for y in range(height):
    the_image.set_pixel(300, y, green_pixel)

the_image.draw(canvas)