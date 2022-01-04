import image

img = image.Image("clownfish.jpg")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)

for x in range(width):
    for y in range(height):
    
        p = img.get_pixel(x, y)

        new_r = 255 - p.get_red()
        new_g = 255 - p.get_green()
        new_b = 255 - p.get_blue()

        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)