import image

rooster = image.Image("rooster.jpg")
rooster_width = rooster.get_width()
rooster_height = rooster.get_height()

smile = image.Image("smile.png")
smile_width = smile.get_width()
smile_height = smile.get_height()

window = image.ImageWin(rooster_width, rooster_height)
rooster.draw(window)

for y in range(smile_height):
    for x in range(smile_width):
        the_pixel = smile.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #manipulate the pixel
        if r < 255 or g < 255 or b < 255:            
            rooster.set_pixel(x + 160, y + 50, the_pixel)
        
    rooster.draw(window)
        
        
        
        
        
        
        
        