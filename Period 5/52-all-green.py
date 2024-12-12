import image

width = 400
height = 200

window = image.ImageWin(width, height)
the_image = image.EmptyImage(width, height)

the_image.draw(window)

                         #R    G    B
green_pixel = image.Pixel(100, 255, 100)

for x in range(width):
    for y in range(height):
        if x % 5 == 0:
            the_image.set_pixel(x, y, green_pixel)


    the_image.draw(window)