from PIL import Image

image = Image.open("C:\\Users\\godpa\\Desktop\\DeletePlz\\figures.png")
left = 270
top = 120
right = 480
bottom = 400
imageCropped = image.crop((left, top, right, bottom))
imageCropped.save("C:\\Users\\godpa\\Desktop\\DeletePlz\\cube.png")
