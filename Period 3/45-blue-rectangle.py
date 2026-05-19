import image

width = 500
height = 100

screen = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

blue_pixel = image.Pixel(0, 0, 255)
for y in range(25, 75):
    for x in range(50, 450):
        img.set_pixel(x, y, blue_pixel)

img.draw(screen)