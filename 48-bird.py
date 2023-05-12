import image

moon = image.Image("bird-far.jpg")
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
        
        average = (r+g+b)/3
        if average > 130:
            new_red = 255
            new_green = 255
            new_blue = 255
        
        else:
            new_red = r
            new_green = g
            new_blue = b
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        moon.set_pixel(x, y, new_pixel)
        
    moon.draw(window)