import image

tree = image.Image("tree.jpg")
width = tree.get_width()
height = tree.get_height()

window = image.ImageWin(width, height)
tree.draw(window)

for x in range(width):
    for y in range(height):
        this_pixel = tree.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
        the_sum = r + b + g
        if the_sum > 300:
            new_pixel = image.Pixel(0, 0, 0)
        else:
            new_pixel = image.Pixel(255, 255, 255)
        
        tree.set_pixel(x, y, new_pixel)
    
    tree.draw(window)
    