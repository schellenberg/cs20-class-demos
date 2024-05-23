import image

flag = image.Image("skflag.png")
width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for x in range(width):
    for y in range(height):
    
        the_pixel = flag.get_pixel(x, y)
        
        #get the colors
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #do some manipulation...
        if r + g + b < 150:
            new_r = 0
            new_g = 0
            new_b = 0
        else:
            new_r = 255
            new_g = 255
            new_b = 255
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        flag.set_pixel(x, y, new_pixel)
        
    flag.draw(canvas)
        
        
        
        
        
    