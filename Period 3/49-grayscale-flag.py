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
        new_r = (r + g + b) / 3
        new_g = (r + g + b) / 3
        new_b = (r + g + b) / 3
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        flag.set_pixel(x, y, new_pixel)
        
    flag.draw(canvas)
        
        
        
        
        
    