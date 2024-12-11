import image

flag = image.Image("skflag.png")

width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for y in range(height):
    for x in range(width):
        the_pixel = flag.get_pixel(x, y)
        
        red = the_pixel.get_red()
        green = the_pixel.get_green()
        blue = the_pixel.get_blue()
        
        # do the pixel manipulation here!
        new_pixel = image.Pixel(255 - red, 255 - green, 255 - blue)
        flag.set_pixel(x, y, new_pixel)
        
    flag.draw(canvas)