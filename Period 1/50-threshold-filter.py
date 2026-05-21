import image

flag = image.Image("skflag.png")
width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for x in range(width):
    for y in range(height):
        this_pixel = flag.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if r + g + b > 200:
            new_pixel = image.Pixel(255, 255, 255)
        else:
            new_pixel = image.Pixel(0, 0, 0)
        
        flag.set_pixel(x, y, new_pixel)
    
    flag.draw(canvas)
        
        
        
        