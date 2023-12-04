import image

width = 200
height = 300

screen = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

img.draw(screen)

for x in range(width):
    for y in range(height):
                               #R  G  B
        the_pixel = image.Pixel(0, 0, 255)
        img.set_pixel(x, y, the_pixel)

    img.draw(screen)
    
    