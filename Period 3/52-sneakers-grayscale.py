import image

sneakers = image.Image("sneakers.jpg")
width = sneakers.get_width()
height = sneakers.get_height()

window = image.ImageWin(width, height)
sneakers.draw(window)

for y in range(height):
    for x in range(width):
        the_pixel = sneakers.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #manipulate the pixel
        if x > width/2:
            new_r = (r + g + b) / 3
            new_g = (r + g + b) / 3
            new_b = (r + g + b) / 3
        
        else:
            new_r = r
            new_g = g
            new_b = b
            
        new_pixel = image.Pixel(new_r, new_g, new_b)
        sneakers.set_pixel(x, y, new_pixel)
        
    sneakers.draw(window)
        
        
        
        
        
        
        
        