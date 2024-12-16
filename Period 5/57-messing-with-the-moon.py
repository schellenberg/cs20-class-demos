import image

moon = image.Image("moon.jpg")
width = moon.get_width()
height = moon.get_height()

window = image.ImageWin(width, height)
moon.draw(window)

for y in range(height):
    for x in range(width):
        the_pixel = moon.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        if r + g + b < 40:
            new_r = 20
            new_g = 30
            new_b = 200
        
        else:
            new_r = r + 100
            new_g = g
            new_b = b
            
        new_pixel = image.Pixel(new_r, new_g, new_b)
        moon.set_pixel(x, y, new_pixel)
    
    moon.draw(window)
        
        

