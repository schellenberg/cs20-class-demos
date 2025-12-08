import image

shoes = image.Image("sneakers.jpg")
width = shoes.get_width()
height = shoes.get_height()

the_window = image.ImageWin(width, height)
shoes.draw(the_window)

for x in range(width):
    for y in range(height):
        the_pixel = shoes.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #image manipulation -- change this!
        gray = (r+g+b)/3
        new_pixel = image.Pixel(gray, gray, gray)
        
        shoes.set_pixel(x, y, new_pixel)
        
    shoes.draw(the_window)
        
        
        