import image

img = image.Image("sneakers.jpg")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)
img.draw(canvas)

for x in range(width):
    for y in range(height):
        the_pixel = img.get_pixel(x, y)
        
        r = the_pixel.get_red()
        g = the_pixel.get_green()
        b = the_pixel.get_blue()
        
        #image processing / mess with the the RGB values...
#         new_r = 255 - r
#         new_g = 255 - g
#         new_b = 255 - b
        average = (r + g + b)/3
        
        new_pixel = image.Pixel(average, average, average)
        img.set_pixel(x, y, new_pixel)
        
    img.draw(canvas)
        
        