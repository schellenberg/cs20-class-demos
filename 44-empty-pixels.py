import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

                        #R   G  B
the_pixel = image.Pixel(50, 180, 20)
for x in range(0, width, 5):
    for y in range(height):
        img.set_pixel(x, y, the_pixel)

    img.draw(canvas)
