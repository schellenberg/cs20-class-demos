import image

shoes = image.Image("sneakers.jpg")
width = shoes.get_width()
height = shoes.get_height()

canvas = image.ImageWin(width, height)
shoes.draw(canvas)

for y in range(height):
    for x in range(width):
        this_pixel = shoes.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if x > width/2:
            average = (r + g + b) / 3
            new_pixel = image.Pixel(average, average, average)
            shoes.set_pixel(x, y, new_pixel)
    
    shoes.draw(canvas)
        