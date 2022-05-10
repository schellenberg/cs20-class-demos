import image

img = image.Image("fish.jpg")

width = img.get_width()
height = img.get_height()

screen = image.ImageWin(width, height)
img.draw(screen)

#loop through all the pixels
for x in range(width):
    for y in range(height):
    
        this_pixel = img.get_pixel(x, y)
        
        red = this_pixel.get_red()
        green = this_pixel.get_green()
        blue = this_pixel.get_blue()
        
        #change the following to make it grayscale!
        average = (red + green + blue) / 3
        new_red = average
        new_green = average
        new_blue = average
        
        new_pixel = image.Pixel(new_red, new_green, new_blue)
        img.set_pixel(x, y, new_pixel)
    
    img.draw(screen)
        