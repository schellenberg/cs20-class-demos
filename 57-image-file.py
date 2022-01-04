import image

img = image.Image("skflag.png")
width = img.get_width()
height = img.get_height()

canvas = image.ImageWin(width, height)

for y in range(height):
    for x in range(width):
        p = img.get_pixel(x, y)

        new_r = p.get_red() - 50
        new_g = p.get_green() - 50
        new_b = p.get_blue() - 50

        new_pixel = image.Pixel(new_r, new_g, new_b)
        img.set_pixel(x, y, new_pixel)

    img.draw(canvas)