import image

width = 400
height = 200

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)
blue_pixel = image.Pixel(0, 0, 255)

for y in range(50, 150):
    for x in range(100, 300):
        img.set_pixel(x, y, blue_pixel)
    
img.draw(canvas)
