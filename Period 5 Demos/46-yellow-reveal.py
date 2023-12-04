import image

width = 200
height = 150

screen = image.ImageWin(width, height)
some_image = image.EmptyImage(width, height)

some_image.draw(screen)
                       # R   G    B
red_pixel = image.Pixel(255, 255, 0)
for x in range(width):
    for y in range(height):
        some_image.set_pixel(x, y, red_pixel)
        
    some_image.draw(screen)