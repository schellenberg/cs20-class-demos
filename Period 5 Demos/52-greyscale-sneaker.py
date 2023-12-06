import image

shoes = image.Image("sneakers.jpg")

height = shoes.get_height()
width = shoes.get_width()

screen = image.ImageWin(width, height)
shoes.draw(screen)

for y in range(height):
    for x in range(width):
        the_pixel = shoes.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        if x > width/2:
            # right side
            average = (r + g + b) / 3
            new_pixel = image.Pixel(average, average, average)
            shoes.set_pixel(x, y, new_pixel)

        
    shoes.draw(screen)