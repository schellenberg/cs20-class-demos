import image

img = image.Image("skflag.png")
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

        #filter
        new_pixel = image.Pixel(r-50, g-50, b-50)
        
        img.set_pixel(x, y, new_pixel)
    
    img.draw(canvas)
    
    
    