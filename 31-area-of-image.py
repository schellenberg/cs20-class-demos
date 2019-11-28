import image

rooster = image.Image("rooster.jpeg")
smile = image.Image("smile.png")

width = rooster.get_width()
height = rooster.get_height()

smile_width = smile.get_width()
smile_height = smile.get_height()

canvas = image.ImageWin(width, height)
rooster.draw(canvas)

for y in range(smile_height):
    for x in range(smile_width):
        this_pixel = smile.get_pixel(x, y)
        
        r = this_pixel.get_red()
        g = this_pixel.get_green()
        b = this_pixel.get_blue()
        
#         if x <= width/2:
#             average = (r + g + b) / 3
#             new_pixel = image.Pixel(average, average, average)
#         else:
#             new_pixel = image.Pixel(r, g, b)
        
        rooster.set_pixel(x, y, this_pixel)
        
    rooster.draw(canvas)
        