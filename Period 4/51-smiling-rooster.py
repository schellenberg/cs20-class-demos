import image

rooster = image.Image("rooster.jpg")
emoji = image.Image("smile.png")

width = rooster.get_width()
height = rooster.get_height()

smile_width = emoji.get_width()
smile_height = emoji.get_height()

the_window = image.ImageWin(width, height)
rooster.draw(the_window)

for y in range(smile_height):
    for x in range(smile_width):
        the_pixel = emoji.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        if r < 255 and g < 255 and b < 255:
            rooster.set_pixel(x + 165, y + 55, the_pixel)
    
    rooster.draw(the_window)
        
        
        
