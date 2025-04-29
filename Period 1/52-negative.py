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
        
        #manipulate pixel here...
        new_pixel = image.Pixel(255-r, 255-g, 255-b)
        
        shoes.set_pixel(x, y, new_pixel)
    
    shoes.draw(window)

#you can save a copy of the image like this...
# shoes.save("negative-shoes.jpg")
        
        