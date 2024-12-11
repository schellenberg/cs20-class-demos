import image

shoes = image.Image("sneakers.jpg")

width = shoes.get_width()
height = shoes.get_height()

canvas = image.ImageWin(width, height)
shoes.draw(canvas)

for y in range(height):
    for x in range(width):
        the_pixel = shoes.get_pixel(x, y)
        
        red = the_pixel.get_red()
        green = the_pixel.get_green()
        blue = the_pixel.get_blue()
        
        # make a grayscale filter
        average = (red + green + blue) / 3
        new_pixel = image.Pixel(average, average, average)
        shoes.set_pixel(x, y, new_pixel)
        
    shoes.draw(canvas)

#save the final version of your manipulation
#shoes.save("grayscale-shoes.jpg")



