import image

flag = image.Image("skflag.png")
width = flag.get_width()
height = flag.get_height()

the_window = image.ImageWin(width, height)
flag.draw(the_window)

for y in range(height):
    for x in range(width):
        the_pixel = flag.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        gray = (r + g + b) / 3
        new_pixel = image.Pixel(gray, gray, gray)
        flag.set_pixel(x, y, new_pixel)
        
    flag.draw(the_window)
    