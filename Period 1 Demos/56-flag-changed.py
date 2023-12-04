import image

flag = image.Image("clownfish.jpg")

width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for y in range(height):
    for x in range(width):
        the_pixel = flag.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()

        #negative image
        new_pixel = image.Pixel(255-r, 255-g, 255-b)
        flag.set_pixel(x, y, new_pixel)
    flag.draw(canvas)
        