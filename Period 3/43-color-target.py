import image

width = 400
height = 200

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

red_pixel = image.Pixel(255, 0, 0)
for x in range(width):
    img.set_pixel(x, 60, red_pixel)
    
green_pixel = image.Pixel(0, 255, 0)
for y in range(height):
    img.set_pixel(350, y, green_pixel)

img.draw(canvas)