import image

flag = image.Image("skflag.png")
width = flag.get_width()
height = flag.get_height()

the_window = image.ImageWin(width, height)
flag.draw(the_window)

for y in range(height):
    for x in range(width):
        the_pixel = flag.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #image manipulation -- change this
        if r + g + b > 200:
            new_pixel = image.Pixel(255, 255, 255)
        else:
            new_pixel = image.Pixel(0, 0, 0)
        
        flag.set_pixel(x, y, new_pixel)
        
    flag.draw(the_window)
    
