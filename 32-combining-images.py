import image

rooster = image.Image("rooster.jpeg")
smile = image.Image("smile.png")

width = rooster.get_width()
height = rooster.get_height()

smile_width = smile.get_width()
smile_height = smile.get_height()

window = image.ImageWin(width, height)
rooster.draw(window)

for x in range(smile_width):
    for y in range(smile_height):
        this_pixel = smile.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        rooster.set_pixel(x + 150, y + 30, this_pixel)
            
    rooster.draw(window)
        