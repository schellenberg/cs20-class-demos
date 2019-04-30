import image

my_image = image.Image("fish.jpg")

width = my_image.get_width()
height = my_image.get_height()

canvas = image.ImageWin(width, height)

for x in range(width):
    for y in range(height):
        p = my_image.get_pixel(x, y)
        
        r = p.get_red()
        g = p.get_green()
        b = p.get_blue()
        
        new_r = 255 - r
        new_g = 255 - g
        new_b = 255 - b
        
        new_pixel = image.Pixel(new_r, new_g, new_b)
        my_image.set_pixel(x, y, new_pixel)

my_image.draw(canvas)