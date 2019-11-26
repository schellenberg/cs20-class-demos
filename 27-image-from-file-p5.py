import image

nemo = image.Image("nemo.jpeg")

width = nemo.get_width()
height = nemo.get_height()

canvas = image.ImageWin(width, height)
nemo.draw(canvas)

for y in range(height):
    for x in range(width):
        this_pixel = nemo.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        new_pixel = image.Pixel(255-r, 255-g, 255-b)
        nemo.set_pixel(x, y, new_pixel)
    nemo.draw(canvas)
    

nemo.save("nightmare.jpg")