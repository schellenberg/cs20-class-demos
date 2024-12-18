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
        
        new_pixel = image.Pixel(red-50, green-50, blue-50)
        flag.set_pixel(x, y, new_pixel)
        
    flag.draw(canvas)
        
        
        