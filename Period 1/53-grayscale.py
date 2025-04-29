import image

rooster = image.Image("rooster.jpg")
width = rooster.get_width()
height = rooster.get_height()

window = image.ImageWin(width, height)
rooster.draw(window)

for y in range(height):
    for x in range(width):
        the_pixel = rooster.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #manipulate pixel here...
        average = (r + g + b) / 3
        new_pixel = image.Pixel(average, average, average)
        
        rooster.set_pixel(x, y, new_pixel)
    
    rooster.draw(window)

#you can save a copy of the image like this...
# rooster.save("negative-rooster.jpg")
        
        