from PIL import Image

image = Image.open("C:\\Users\\godpa\\Desktop\\DeletePlz\\screenshot.jpg")
imageBW = image.convert("L")
imageBW.save("C:\\Users\\godpa\\Desktop\\DeletePlz\\screenshot_bw.jpg")
