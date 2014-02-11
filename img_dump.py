# This is a script to dump the raw data from an image file.

import sys
from PIL import Image

fileName = sys.argv[1]

image = Image.open(fileName)

with open(fileName + ".dump", 'wb') as output:
    for pixel in image.getdata():
        output.write(bytes(pixel))

with open(fileName + ".meta", 'w') as meta:
    meta.write("{0}\n".format(image.size[0]))
    meta.write("{0}\n".format(image.size[1]))
