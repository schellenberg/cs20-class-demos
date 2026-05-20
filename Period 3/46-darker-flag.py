import image

flag = image.Image("skflag.png")
width = flag.get_width()
height = flag.get_height()

screen = image.ImageWin(width, height)
flag.draw(screen)

for y in range(height):
    for x in range(width):
        this_pixel = flag.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
                               # R    G      B
        new_pixel = image.Pixel(r-50, g-50, b-50)
        flag.set_pixel(x, y, new_pixel)
    
    flag.draw(screen)
