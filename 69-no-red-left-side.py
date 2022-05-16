import image

img = image.Image("berries.jpg")
width = img.get_width()
height = img.get_height()

win = image.ImageWin(width, height)
img.draw(win)

for y in range(height):
    for x in range(width):
        this_pixel = img.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if x < width/2:
            r = 0
            
        new_pixel = image.Pixel(r, g, b)
        img.set_pixel(x, y, new_pixel)

    img.draw(win)
