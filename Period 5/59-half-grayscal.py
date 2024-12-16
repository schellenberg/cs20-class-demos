import image

shoes = image.Image("sneakers.jpg")
width = shoes.get_width()
height = shoes.get_height()

window = image.ImageWin(width, height)
shoes.draw(window)

for y in range(height):
    for x in range(width):
        the_pixel = shoes.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #make the right side of the image grayscale
        #leave the left side normal
        if x > width/2:
            average = (r + g + b) / 3
            new_r = average
            new_g = average
            new_b = average
        
        else:
            new_r = r
            new_g = g
            new_b = b
            
        new_pixel = image.Pixel(new_r, new_g, new_b)
        shoes.set_pixel(x, y, new_pixel)
    
    shoes.draw(window)
        
        



