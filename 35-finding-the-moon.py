import image

img = image.Image("moon.jpg")
width = img.get_width()
height = img.get_height()

window = image.ImageWin(width, height)
img.draw(window)

for y in range(height):
    for x in range(width):    
        this_pixel = img.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if r + g + b <= 50:
            new_r = 0
            new_g = 255
            new_b = 0
        else:
            new_r = r
            new_g = g
            new_b = b

        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)
        
    img.draw(window)