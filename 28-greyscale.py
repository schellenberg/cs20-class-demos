import image

flower = image.Image("flower.jpg")
width = flower.get_width()
height = flower.get_height()

window = image.ImageWin(width, height)
flower.draw(window)



for y in range(height):
    for x in range(width):
        this_pixel = flower.get_pixel(x, y)

        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        grey = (r + g + b) / 3
        
        new_pixel = image.Pixel(grey, grey, grey)
        
        flower.set_pixel(x, y, new_pixel)
        
    flower.draw(window)