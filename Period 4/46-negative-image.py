import image

pineapple = image.Image("pineapples.jpg")

width = pineapple.get_width()
height = pineapple.get_height()

canvas = image.ImageWin(width, height)
pineapple.draw(canvas)

for y in range(height):
    for x in range(width):
        the_pixel = pineapple.get_pixel(x, y)
        
        red = the_pixel.get_red()
        green = the_pixel.get_green()
        blue = the_pixel.get_blue()
        
        new_pixel = image.Pixel(255-red, 255-green, 255-blue)
        
        pineapple.set_pixel(x, y, new_pixel)
    
    pineapple.draw(canvas)
        
        
        
