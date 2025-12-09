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
        
        if r + g + b > 30:
            new_pixel = image.Pixel(r, g, b+50)
            moon.set_pixel(x, y, new_pixel)
    
    moon.draw(window)
    
        
        