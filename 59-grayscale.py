import image

img = image.Image("clownfish.jpg")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)

for x in range(width):
    for y in range(height):
    
        p = img.get_pixel(x, y)

        new_r = p.get_red()
        new_g = p.get_green()
        new_b = p.get_blue()

        average = (new_r + new_g + new_b) / 3

        new_pixel = image.Pixel(average, average, average)
        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)