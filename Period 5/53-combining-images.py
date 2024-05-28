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
        this_pixel = smile.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if r < 250 or g < 250 or b < 250:
            #not on the white part...
            rooster.set_pixel(x + 170, y + 60, this_pixel)
        
    rooster.draw(window)
        

