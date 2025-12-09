import image

shoes = image.Image("sneakers.jpg")
width = shoes.get_width()
height = shoes.get_height()

window = image.ImageWin(width, height)
shoes.draw(window)

for y in range(height):
    for x in range(width):
        this_pixel = shoes.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        if x > width/2:
            gray = (r+g+b)/3
            new_pixel = image.Pixel(gray, gray, gray)
            shoes.set_pixel(x, y, new_pixel)
    
    shoes.draw(window)
        
