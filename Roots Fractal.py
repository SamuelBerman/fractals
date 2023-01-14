from PIL import Image
import itertools
import numpy as np
from datetime import datetime
import os


degree = 16

width = 3840
height = 2160

img = Image.new('HSV', (width, height), (0, 0, 0))
pixels = img.load()

scale = height / 4
x_off = width / 2
y_off = height / 2


for perm in itertools.product((-1, 1), repeat=degree):
    for root in np.roots(perm):
        x = root.real * scale + x_off
        y = root.imag * scale + y_off

        if root.imag != 0:
            pixel = pixels[x, height - y - 1]
            pixels[x, height - y - 1] = (pixel[0] + 1, 255, 255)


img = img.convert("RGB")

resolution = str(width) + 'x' + str(height)
time = str(datetime.now().strftime('%Y.%m.%d %H.%M.%S'))
filename = 'roots' + ' ' + resolution + ' ' + time + '.png'
path = os.path.join(os.path.dirname(__file__), 'fractal_images', filename)

img.save(path)

img.show()
