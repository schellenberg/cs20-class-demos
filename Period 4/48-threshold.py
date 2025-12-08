import image

shoes = image.Image("skflag.png")
width = shoes.get_width()
height = shoes.get_height()

the_window = image.ImageWin(width, height)
shoes.draw(the_window)

for x in range(width):
    for y in range(height):
        the_pixel = shoes.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #image manipulation -- change this!
        if r + g + b > 150:
            new_pixel = image.Pixel(255, 255, 255)
        else:
            new_pixel = image.Pixel(0, 0, 0)
        
        shoes.set_pixel(x, y, new_pixel)
        
    shoes.draw(the_window)
        
        
    