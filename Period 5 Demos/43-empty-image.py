import image

width = 1000
height = 500

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

                        #R  G  B
some_pixel = image.Pixel(0, 0, 255)
for y in range(height):
    img.set_pixel(200, y, some_pixel)

img.draw(canvas)