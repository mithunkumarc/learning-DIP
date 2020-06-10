from PIL import Image

# for full path : c:\\path\\image.png
img = Image.open('lena_gray.png')

# resize
size = (150,150)
smaller_img = img.resize(size)
smaller_img.show()

#crop
box = (100,100,400,400)
crop_img = img.crop(box)
crop_img.show()

#rotate
rotated_img = img.rotate(45)
rotated_img.show()
