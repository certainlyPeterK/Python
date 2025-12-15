from PIL import Image, ImageFont, ImageDraw

pixels = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1, 1, 1, 0, 1],
          [1, 1, 1, 0, 0, 0, 1, 1, 1],
          [1, 1, 0, 1, 0, 1, 0, 1, 1],
          [1, 1, 0, 0, 1, 0, 0, 1, 1],
          [1, 1, 0, 1, 0, 1, 0, 1, 1],
          [1, 1, 1, 0, 0, 0, 1, 1, 1],
          [1, 0, 1, 1 ,1, 1, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1]]

image = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(image)
pixel_size = 10
for y, row in enumerate(pixels):
    for x, pixel in enumerate(row):
        print(pixel)
        top_left = (x*pixel_size, y*pixel_size)
        bottom_right = ((x+1)*pixel_size, (y+1)*pixel_size)
        color = "black" if pixel == 1 else "white"
        draw.rectangle([top_left, bottom_right], fill=color)
image.show()
image.save("C:\\Users\\godpa\\Desktop\\DeletePlz\\my pixels pict.png")
