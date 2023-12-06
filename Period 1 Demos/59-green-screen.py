import image

moon = image.Image("moon.jpg")

width = moon.get_width()
height = moon.get_height()

canvas = image.ImageWin(width, height)
moon.draw(canvas)

for y in range(height):
    for x in range(width):
        the_pixel = moon.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        if r < 20 and g < 20 and b < 20:
            #pixel pretty dark       R   G  B
            new_pixel = image.Pixel(255, 0, 0)
            moon.set_pixel(x, y, new_pixel)
    
    moon.draw(canvas)
            
        
        