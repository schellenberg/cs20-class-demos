import image

shoes = image.Image("sneakers.jpg")
width = shoes.get_width()
height = shoes.get_height()

screen = image.ImageWin(width, height)
shoes.draw(screen)

for y in range(height):
    for x in range(width):
        this_pixel = shoes.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        #filter
        average = (r + g + b) / 3        
        new_pixel = image.Pixel(average, average, average)
        
        shoes.set_pixel(x, y, new_pixel)
        
    shoes.draw(screen)
        