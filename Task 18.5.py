from PIL import Image, ImageFont, ImageDraw

image = Image.open("C:\\Users\\godpa\\Desktop\\DeletePlz\\pixels.png")
draw = ImageDraw.Draw(image)
draw.rectangle((178, 35, 221, 80), outline="red", fill="red")
draw.rectangle((23, 150, 51, 230), outline="blue", fill="blue")
image.save("C:\\Users\\godpa\\Desktop\\DeletePlz\\pixels_ready.png")
