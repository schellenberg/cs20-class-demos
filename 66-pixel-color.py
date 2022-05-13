import image

img = image.Image("bird-far.jpg")

width = img.get_width()
height = img.get_height()

window = image.ImageWin(width, height)
img.draw(window)

for y in range(height):
    for x in range(width):
        pixel = img.get_pixel(x, y)
        
        r = pixel.get_red()
        g = pixel.get_green()
        b = pixel.get_blue()
        
        #filter
        if r + g + b > 400:
            r = 255
            g = 255
            b = 255
                            
        new_pixel = image.Pixel(r, g, b)
        img.set_pixel(x, y, new_pixel)
        
    img.draw(window)
    
    