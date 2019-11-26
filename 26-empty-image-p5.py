import image

width = 300
height = 200

canvas = image.ImageWin(width, height)

my_image = image.EmptyImage(width, height)

this_pixel = image.Pixel(255, 0, 0)
other_pixel = image.Pixel(0, 0, 255)

for y in range(height):
    for x in range(width):
        
        if y % 5 == 0:
            my_image.set_pixel(x, y, other_pixel)
        else:
            my_image.set_pixel(x, y, this_pixel)
        

    my_image.draw(canvas)