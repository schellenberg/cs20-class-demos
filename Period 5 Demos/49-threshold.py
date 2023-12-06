import image

the_image = image.Image("skflag.png")

width = the_image.get_width()
height = the_image.get_height()

screen = image.ImageWin(width, height)
the_image.draw(screen)

for x in range(width):
    for y in range(height):
        the_pixel = the_image.get_pixel(x, y)

        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        # image manipulation here!
        if r + g + b < 200:
            new_pixel = image.Pixel(0, 0, 0)
        else:
            new_pixel = image.Pixel(255, 255, 255)
        
        the_image.set_pixel(x, y, new_pixel)
    
    the_image.draw(screen)
        
        
        
        
        
        