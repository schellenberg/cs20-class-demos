import image

flag = image.Image("skflag.png")

width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for y in range(height):
    for x in range(width):
        current_pixel = flag.get_pixel(x, y)
        r = current_pixel.get_red()
        g = current_pixel.get_green()
        b = current_pixel.get_blue()
        
        the_pixel = image.Pixel(255 - r, 255 - g, 255 - b)
        
        flag.set_pixel(x, y, the_pixel)
    
    flag.draw(canvas)
    
