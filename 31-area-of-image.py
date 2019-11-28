import image

moon = image.Image("sneakers.jpeg")

width = moon.get_width()
height = moon.get_height()

canvas = image.ImageWin(width, height)
moon.draw(canvas)

for y in range(height):
    for x in range(width):
        this_pixel = moon.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if x <= width/2:
            average = (r + g + b) / 3
            new_pixel = image.Pixel(average, average, average)
        else:
            new_pixel = image.Pixel(r, g, b)
        
        moon.set_pixel(x, y, new_pixel)
        
    moon.draw(canvas)
        