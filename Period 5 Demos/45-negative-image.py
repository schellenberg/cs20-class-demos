import image

img = image.Image("clownfish.jpg")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)
img.draw(canvas)

for y in range(height):
    for x in range(width):
        this_pixel = img.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()

        #filter - invert/negative
        new_pixel = image.Pixel(255-r, 255-g, 255-b)
        
        img.set_pixel(x, y, new_pixel)
    
    img.draw(canvas)
    
    
    