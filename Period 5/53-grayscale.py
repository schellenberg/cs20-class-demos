import image

rooster = image.Image("rooster.jpg")
width = rooster.get_width()
height = rooster.get_height()

canvas = image.ImageWin(width, height)
rooster.draw(canvas)

for y in range(height):
    for x in range(width):
        this_pixel = rooster.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        #image manipulation goes here!
        average = (r + g + b) / 3
        new_pixel = image.Pixel(average, average, average)
        
        rooster.set_pixel(x, y, new_pixel)
    
    rooster.draw(canvas)
        
#save the image like this...
# rooster.save("negative-rooster.jpg")

