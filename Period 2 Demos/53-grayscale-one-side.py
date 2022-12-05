import image

feet = image.Image("sneakers.jpg")
width = feet.get_width()
height = feet.get_height()

canvas = image.ImageWin(width, height)
feet.draw(canvas)

for y in range(height):
    for x in range(width):
        this_pixel = feet.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if x > width/2:
            average = (r + g + b) / 3        
            new_pixel = image.Pixel(average, average, average)
            feet.set_pixel(x, y, new_pixel)
            
    feet.draw(canvas)
