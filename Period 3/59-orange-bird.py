import image

bird = image.Image("bird-far.jpg")
width = bird.get_width()
height = bird.get_height()

window = image.ImageWin(width, height)
bird.draw(window)

for y in range(height):
    for x in range(width):
        the_pixel = bird.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #image manipulation
        if r + g + b < 250:
            new_r = 180
            new_g = 75
            new_b = 0
        else:
            new_r = 255
            new_g = 255
            new_b = 255
            
        new_pixel = image.Pixel(new_r, new_g, new_b)
        bird.set_pixel(x, y, new_pixel)
    
    bird.draw(window)
            
            
            
