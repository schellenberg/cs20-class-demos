import image

sneakers = image.Image("sneakers.jpg")

width = sneakers.get_width()
height = sneakers.get_height()

canvas = image.ImageWin(width, height)
sneakers.draw(canvas)

for y in range(height):
    for x in range(width):
        current_pixel = sneakers.get_pixel(x, y)
        
        r = current_pixel.get_red()
        g = current_pixel.get_green()
        b = current_pixel.get_blue()
        
        the_pixel = image.Pixel(255 - r, 255 - g, 255 - b)
        sneakers.set_pixel(x, y, the_pixel)        
        
    sneakers.draw(canvas)