import image

img = image.Image("rooster.jpg")
img_to_add = image.Image("smile.png")

width = img.get_width()
height = img.get_height()

width_small = img_to_add.get_width()
height_small = img_to_add.get_height()

window = image.ImageWin(width, height)
img.draw(window)

for x in range(width_small):
    for y in range(height_small):
    
        pixel = img_to_add.get_pixel(x, y)
        
        r = pixel.get_red()
        g = pixel.get_green()
        b = pixel.get_blue()
        
        #filter
        if r < 250 and g < 250 and b < 250:
            img.set_pixel(x + 175, y + 60, pixel)
        
    img.draw(window)
    
    