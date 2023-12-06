import image

moon = image.Image("sneakers.jpg")

width = moon.get_width()
height = moon.get_height()

canvas = image.ImageWin(width, height)
moon.draw(canvas)

for y in range(height):
    for x in range(width):
        the_pixel = moon.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        if x > width/2:
            #right side of the image
            average = (r + g + b) / 3
            new_pixel = image.Pixel(average, average, average)
            moon.set_pixel(x, y, new_pixel)
    
    moon.draw(canvas)
            
        
        