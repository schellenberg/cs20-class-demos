import image

img = image.Image("skflag.png")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)

img.draw(canvas)

for y in range(height):
    for x in range(width):
        p = img.get_pixel(x, y)
        
        r = p.get_red()
        g = p.get_green()
        b = p.get_blue()
        
        if r + g + b > 200:
            new_r = 0
            new_g = 0
            new_b = 0
        else:
            new_r = 255
            new_g = 255
            new_b = 255
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)
    