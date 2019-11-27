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
        
        if r + g + b >= 200:
            new_pixel = image.Pixel(0, 0, 0)
        else:
            new_pixel = image.Pixel(255, 255, 255)
        
        flower.set_pixel(x, y, new_pixel)
        
    flower.draw(window)