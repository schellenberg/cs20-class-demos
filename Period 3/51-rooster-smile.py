import image

rooster = image.Image("rooster.jpg")
rooster_width = rooster.get_width()
rooster_height = rooster.get_height()

smile = image.Image("smile.png")
smile_width = smile.get_width()
smile_height = smile.get_height()

canvas = image.ImageWin(rooster_width, rooster_height)
rooster.draw(canvas)

#look at every pixel in the emoji
for x in range(smile_width):
    for y in range(smile_height):
        this_pixel = smile.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if r < 250 and g < 250 and b < 250:
            rooster.set_pixel(x + 180, y + 60, this_pixel)
    
    rooster.draw(canvas)
        