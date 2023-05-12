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
        
        if r <= 20 and g <= 20 and b <= 20:
            new_red = 0
            new_green = 0
            new_blue = 100
        
        else:
            new_red = r + 150
            new_green = g
            new_blue = b
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        moon.set_pixel(x, y, new_pixel)
        
    moon.draw(window)