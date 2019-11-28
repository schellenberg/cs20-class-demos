import image

moon = image.Image("bird-far.jpeg")

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
        
        if r + g + b >= 400:
            new_pixel = image.Pixel(255, 255, 255)
            moon.set_pixel(x, y, new_pixel)
            
    moon.draw(window)
        