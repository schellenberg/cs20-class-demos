import image

width = 1000
height = 500

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)


#intersecting lines

#                         #R  G  B
# some_pixel = image.Pixel(0, 0, 255)
# for y in range(height):
#     img.set_pixel(700, y, some_pixel)
# 
# red_pixel = image.Pixel(255, 0, 0)
# for x in range(width):
#     img.set_pixel(x, 100, red_pixel)

mystery = image.Pixel(255, 0, 255)
for x in range(300):
    for y in range(200):
        img.set_pixel(x, y, mystery)

    img.draw(canvas)

