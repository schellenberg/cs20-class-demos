import image

width = 200
height = 100

window = image.ImageWin(width, height)
blue_rectangle = image.EmptyImage(width, height)

blue_pixel = image.Pixel(0, 0, 255)
for x in range(width):
    for y in range(height):
        blue_rectangle.set_pixel(x, y, blue_pixel)

    blue_rectangle.draw(window)