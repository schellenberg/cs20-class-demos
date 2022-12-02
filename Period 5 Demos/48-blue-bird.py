import image

moon = image.Image("moon.jpg")
width = moon.get_width()
height = moon.get_height()

window = image.ImageWin(width, height)
moon.draw(window)

for x in range(width):
    for y in range(height):
        current_pixel = moon.get_pixel(x, y)
        
        r = current_pixel.get_red()
        g = current_pixel.get_green()
        b = current_pixel.get_blue()
        
        if r + g + b > 80:
            new_pixel = image.Pixel(r, g, b+45)
            moon.set_pixel(x, y, new_pixel)
    moon.draw(window)
            
        