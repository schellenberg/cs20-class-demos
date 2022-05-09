import image

img = image.Image("fish.jpg")

width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)
img.draw(canvas)

#loop through every pixel
for y in range(height):
    for x in range(width):
        p = img.get_pixel(x, y)
        
        r = p.get_red()
        g = p.get_green()
        b = p.get_blue()
        
        new_pixel = image.Pixel(r-50, g-50, b-50)
        img.set_pixel(x, y, new_pixel)
        
    img.draw(canvas)