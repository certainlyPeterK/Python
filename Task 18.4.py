from PIL import Image, ImageFont, ImageDraw

image = Image.new("RGB", (200, 200), "black")
font = ImageFont.truetype("C:\\WINDOWS\\FONTS\\IMPACT.TTF")
draw = ImageDraw.Draw(image)
draw.text((100, 100), "Пётр был здесь...", font=font)
image.show()
image.save("C:\\Users\\godpa\\Desktop\\DeletePlz\\Ваше_имя был здесь.png")
