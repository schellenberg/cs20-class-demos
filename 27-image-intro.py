import image

width = 500
height = 400

canvas = image.ImageWin(width, height)
my_image = image.EmptyImage(width, height)

for x in range(width):
    for y in range(height):
        this_pixel = image.Pixel(50, 50, 50)
        my_image.set_pixel(x, y, this_pixel)

    my_image.draw(canvas)