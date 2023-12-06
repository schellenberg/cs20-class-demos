import image

bird = image.Image("bird-far.jpg")

height = bird.get_height()
width = bird.get_width()

screen = image.ImageWin(width, height)
bird.draw(screen)

for x in range(width):
    for y in range(height):
        the_pixel = bird.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        if r + g + b > 200:
            # not bird
            new_pixel = image.Pixel(255, 255, 255)
            bird.set_pixel(x, y, new_pixel)

        
    bird.draw(screen)