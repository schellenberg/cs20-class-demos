import image

width = 400
height = 300

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

for y in range(height):
    for x in range(width):
        if y % 3 == 0:
            p = image.Pixel(255, 0, 0)
            img.set_pixel(x, y, p)

    img.draw(canvas)
