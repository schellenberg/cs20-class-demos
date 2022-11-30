import image

width = 800
height = 400

canvas = image.ImageWin(width, height)
img = image.EmptyImage(width, height)

                        #R  G  B
some_pixel = image.Pixel(0, 0, 255)

#two lines intersecting
# for y in range(height):
#     img.set_pixel(50, y, some_pixel)
# 
# for x in range(width):
#     img.set_pixel(x, 300, some_pixel)

#changing every pixel in the image
for y in range(height):
    for x in range(width):
        img.set_pixel(x, y, some_pixel)

img.draw(canvas)
