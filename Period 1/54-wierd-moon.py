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
        
        #manipulate pixel here...
        if x < width/2 and r < 20 and g < 20 and b < 20:
            new_pixel = image.Pixel(255, 0, 0)
        elif x >= width/2 and r < 20 and g < 20 and b < 20:
            new_pixel = image.Pixel(0, 255, 0)
        else:
            new_pixel = image.Pixel(r, g, b + 100)
        moon.set_pixel(x, y, new_pixel)
    
    moon.draw(window)
