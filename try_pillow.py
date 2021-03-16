from PIL import Image, ImageDraw

img = Image.new("RGB", (640, 480), (127, 127, 0))
d = ImageDraw.Draw(img)
d.text((10, 10), "Hello World", fill=(255, 255, 0))
img.show()
img.save("out.jpg")
