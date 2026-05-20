import image

rooster = image.Image("rooster.jpg")
width = rooster.get_width()
height = rooster.get_height()

screen = image.ImageWin(width, height)
rooster.draw(screen)

for y in range(height):
    for x in range(width):
        this_pixel = rooster.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        new_pixel = image.Pixel(255-r, 255-g, 255-b)
        rooster.set_pixel(x, y, new_pixel)
    rooster.draw(screen)
        