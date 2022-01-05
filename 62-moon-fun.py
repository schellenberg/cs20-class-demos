import image

img = image.Image("bird-far.jpg")
width = img.get_width()
height = img.get_height()

window = image.ImageWin(width, height)
img.draw(window)

#look at every pixel
for y in range(height):
    for x in range(width):
        this_pixel = img.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if r + g + b < 150:
            new_r = 255
            new_g = 0
            new_b = 0
        else:
            new_r = 255
            new_g = 255
            new_b = 255
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)
    
    img.draw(window)
        