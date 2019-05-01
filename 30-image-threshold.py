import image

my_image = image.Image("skflag.png")

width = my_image.get_width()
height = my_image.get_height()

canvas = image.ImageWin(width, height)

for x in range(width):
    for y in range(height):
        p = my_image.get_pixel(x, y)
        
        r = p.get_red()
        g = p.get_green()
        b = p.get_blue()
        
        if (r + g + b > 200):
            new_pixel = image.Pixel(0, 0, 0)
        else:
            new_pixel = image.Pixel(255, 255, 255)
        
        my_image.set_pixel(x, y, new_pixel)

    my_image.draw(canvas)
