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
        
        #image manipulation goes here!
        new_pixel = image.Pixel(255-r, 255-g, 255-b)
        
        shoes.set_pixel(x, y, new_pixel)
    
    shoes.draw(canvas)
        
#save the image like this...
shoes.save("negative-shoes.jpg")
