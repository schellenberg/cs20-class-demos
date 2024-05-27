import image

flag = image.Image("skflag.png")
width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)


for x in range(width):
    for y in range(height):
        the_pixel = flag.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #manipulate the pixels here...
        new_r = (r+b+g)/3
        new_g = (r+b+g)/3
        new_b = (r+b+g)/3
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        flag.set_pixel(x, y, new_pixel)
        
    flag.draw(canvas)
        
        
        
        
        
        
        
        

