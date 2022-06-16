from PIL import Image

im = Image.open('bw_template.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
pix = im.load()

print (width, height)
print (pixel_values)
print (pix)