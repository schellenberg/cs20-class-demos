import image

flag = image.Image("sneakers.jpg")
width = flag.get_width()
height = flag.get_height()

canvas = image.ImageWin(width, height)
flag.draw(canvas)

for y in range(height):
    for x in range(width):
        p = flag.get_pixel(x, y)
        
        r = p.get_red()
        g = p.get_green()
        b = p.get_blue()
        
        #0.299 R + 0.587 G + 0.114 B
        average = 0.299*r + 0.587*g + 0.114*b
        
        new_pixel = image.Pixel(average, average, average)
        
        flag.set_pixel(x, y, new_pixel)
    
    flag.draw(canvas)

# get_pixel()
# get_red()  get_green()   get_blue()
# image.Pixel(r, g, b)
# set_pixel(x, y, pixel)