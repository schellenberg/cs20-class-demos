import image

img = image.Image("sneakers.jpg")

width = img.get_width()
height = img.get_height()

window = image.ImageWin(width, height)
img.draw(window)

for x in range(width):
    for y in range(height):
    
        pixel = img.get_pixel(x, y)
        
        r = pixel.get_red()
        g = pixel.get_green()
        b = pixel.get_blue()
        
        #filter
        if y > height/2:
            average = (r + g + b) / 3
            r = average
            g = average
            b = average
                            
        new_pixel = image.Pixel(r, g, b)
        img.set_pixel(x, y, new_pixel)
        
    img.draw(window)
    
    