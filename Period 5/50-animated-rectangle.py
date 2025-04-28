import image

width = 150
height = 200

screen = image.ImageWin(width, height)
filled_rectangle = image.EmptyImage(width, height)

green_pixel = image.Pixel(0, 255, 0)
for x in range(width):
    for y in range(height):
        filled_rectangle.set_pixel(x, y, green_pixel)
    
    filled_rectangle.draw(screen)