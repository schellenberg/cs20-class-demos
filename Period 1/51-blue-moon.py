import image

moon = image.Image("moon.jpg")
width = moon.get_width()
height = moon.get_height()

canvas = image.ImageWin(width, height)
moon.draw(canvas)

for x in range(width):
    for y in range(height):
        this_pixel = moon.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if r + g + b > 50:
            new_pixel = image.Pixel(r, g, b+50)
        else:
            new_pixel = image.Pixel(150, 0, 0)
        
        moon.set_pixel(x, y, new_pixel)
    
    moon.draw(canvas)
        
        
        
        
