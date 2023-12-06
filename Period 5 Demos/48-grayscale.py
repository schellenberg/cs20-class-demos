import image

the_image = image.Image("sneakers.jpg")

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
        new_r = (r+g+b)/3 
        new_g = (r+g+b)/3
        new_b = (r+g+b)/3
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        the_image.set_pixel(x, y, new_pixel)
    
    the_image.draw(screen)
        
        
        
        
        
        