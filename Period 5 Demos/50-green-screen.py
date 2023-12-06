import image

moon = image.Image("moon.jpg")

height = moon.get_height()
width = moon.get_width()

screen = image.ImageWin(width, height)
moon.draw(screen)

for x in range(width):
    for y in range(height):
        the_pixel = moon.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        if r + g + b < 30:
            # pretty dark pixel
            new_pixel = image.Pixel(60, 60, 60)
            moon.set_pixel(x, y, new_pixel)
            
        else:
            #moon
            new_pixel = image.Pixel(r, g, b + 50)
            moon.set_pixel(x, y, new_pixel)
        
    moon.draw(screen)