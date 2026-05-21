import image

flag = image.Image("skflag.png")
width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for x in range(width):
    for y in range(height):
        pixel = flag.get_pixel(x, y)
        
        r = pixel.get_red()
        g = pixel.get_green()
        b = pixel.get_blue()
        
        average = (r + g + b) / 3
        if average > 50:
            new_pixel = image.Pixel(255, 255, 255)
        else:
            new_pixel = image.Pixel(0, 0, 0)
            
        flag.set_pixel(x, y, new_pixel)
    
    flag.draw(canvas)