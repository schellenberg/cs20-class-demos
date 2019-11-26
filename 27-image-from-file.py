import image

img = image.Image("fish.jpeg")

width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)

for x in range(width):
    for y in range(height):
        p = img.get_pixel(x, y)
        
        r = p.get_red()
        g = p.get_green()
        b = p.get_blue()
        
        new_pixel = image.Pixel(255-r, 255-g, 255-b)
        
        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)
    
img.save("negative.jpg")