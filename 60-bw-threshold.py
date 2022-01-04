import image

img = image.Image("skflag.png")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)

for x in range(width):
    for y in range(height):
    
        p = img.get_pixel(x, y)

        new_r = p.get_red()
        new_g = p.get_green()
        new_b = p.get_blue()

        the_sum = new_r + new_g + new_b
        if the_sum < 300:
            new_pixel = image.Pixel(0, 0, 0)
        else:
            new_pixel = image.Pixel(255, 255, 255)
        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)