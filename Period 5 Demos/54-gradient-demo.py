import image

def distance(x1, y1, x2, y2):
    x_diff = x2 - x1
    y_diff = y2 - y1
    
    square = x_diff ** 2 + y_diff ** 2
    return square ** (1/2)

width = 500
height = 500

canvas = image.ImageWin(width, height)
gradient = image.EmptyImage(width, height)

gradient.draw(canvas)

centre_x = width/2
centre_y = height/2

for x in range(width):
    for y in range(height):
        r = 150
        g = 50
        b = distance(x, y, centre_x, centre_y)
        
        the_pixel = image.Pixel(r, g, b)
        gradient.set_pixel(x, y, the_pixel)
    
gradient.draw(canvas)
