import image

width = 800
height = 400

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

some_pixel = image.Pixel(255, 0, 0)

for x in range(width):
    img.set_pixel(x, 300, some_pixel)

img.draw(canvas)
