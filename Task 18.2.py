from PIL import Image

image = Image.open("C:\\Users\\godpa\\Desktop\\Somewhere\\screen_camera.png")
imageRotated = image.rotate(180)
imageRotated.save("C:\\Users\\godpa\\Desktop\\DeletePlz\\screen_camera.png")
