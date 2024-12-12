import image

the_flag = image.Image("skflag.png")
width = the_flag.get_width()
height = the_flag.get_height()

canvas = image.ImageWin(width, height)
the_flag.draw(canvas)

for y in range(height):
    for x in range(width):
        the_pixel = the_flag.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #image manipulation here
        if r + g + b > 150:
            new_pixel = image.Pixel(0, 0, 0)
        else:
            new_pixel = image.Pixel(255, 255, 255)
        
        the_flag.set_pixel(x, y, new_pixel)
    
    the_flag.draw(canvas)
        
        
        
        
        