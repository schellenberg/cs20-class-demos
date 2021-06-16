import image

img = image.Image("sneakers.jpg")
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
        
        if x < width/2:
            new_r = g
            new_g = b
            new_b = r
        else:
            new_r = (r+b+g)/3
            new_g = (r+b+g)/3
            new_b = (r+b+g)/3

        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)
        
    img.draw(window)