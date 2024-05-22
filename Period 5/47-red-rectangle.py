import image

width = 250
height = 200

window = image.ImageWin(width, height)
my_image = image.EmptyImage(width, height)

red_pixel = image.Pixel(255, 0, 0)
for y in range(height):
    for x in range(width):
        my_image.set_pixel(x, y, red_pixel)

    my_image.draw(window)