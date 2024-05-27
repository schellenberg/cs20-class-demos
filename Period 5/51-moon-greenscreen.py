import image

moon = image.Image("moon.jpg")
width = moon.get_width()
height = moon.get_height()

window = image.ImageWin(width, height)
moon.draw(window)

for x in range(width):
    for y in range(height):
        this_pixel = moon.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        #image manipulation
        if r + g + b > 30:
            new_r = r
            new_g = g
            new_b = b + 100
            
        else:
            new_r = r
            new_g = g
            new_b = b
            
        new_pixel = image.Pixel(new_r, new_g, new_b)
        moon.set_pixel(x, y, new_pixel)
        
    moon.draw(window)
        

