# Get image from url and make it white background
import requests
link = 'https://www.tanoshiijapanese.com/images/standard/j/20908.png'

response = requests.get(link)

file = open("sample_image.png", "wb")
file.write(response.content)
file.close()

from PIL import Image

img = Image.open('sample_image.png')
img = img.convert("RGBA")

pixdata = img.load()

width, height = img.size
for y in range(height):
    for x in range(width):
        if pixdata[x, y] == (0, 0, 0, 0):
            pixdata[x, y] = (230, 230, 230, 255)
        # print(pixdata[x, y])

img.save("img2.jpg", "PNG")

image = Image.open('sample_image.png')
new_image = Image.new("RGBA", image.size, "WHITE") # Create a white rgba background
new_image.paste(image, (0, 0), image)              # Paste the image on the background. Go to the links given below for details.
new_image.convert('RGB').save('test.jpg', "JPEG")  # Save as JPEG