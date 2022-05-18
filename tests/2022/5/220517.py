# Get image pixels and cut it

from PIL import Image
import math

img = Image.open('test.jpg')
print(img.width)
n_squares = math.floor(img.width / 110)
# print(img.height)
# im.crop((left, top, right, bottom))
half_w1 = math.ceil(n_squares/2*110+n_squares/2*4)
half_w2 = math.ceil(n_squares/2*110+n_squares/2*3)
half_h = math.floor(img.height/2) + 1
im1 = img.crop((0, 0, half_w1, half_h-2))
im2 = img.crop((half_w2, 0, img.width, half_h))
#im2 = img.crop(math.ceil(n_squares/2*110+n_squares/2*4), 0, img.width, math.ceil(img.height/2))
 
# Shows the image in image viewer
im1.save('im1.jpg')
im2.save('im2.jpg')

#resize, first image
#image1 = image1.resize((426, 240))
im1_size = im1.size
im2_size = im2.size
new_image = Image.new('RGB',(im1_size[0], im1_size[1]*2), (250,250,250))
new_image.paste(im1,(0,0))
new_image.paste(im2,(0,im1_size[1]))
new_image.save("merged_image.jpg","JPEG")
#new_image.show()