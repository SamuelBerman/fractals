from PIL import Image
import math
from datetime import datetime
import os


iterations = 50

width = 500
height = 500

background = (0, 0, 0)
foreground = (0, 0, 0)

img = Image.new('HSV', (width, height), background)
pixels = img.load()


def get_color(cycles):
    normalized = math.log(cycles+1) / math.log(iterations)
    return (round(0.6*255), round(0.9*255), round(normalized*128))


for y in range(height):
    for x in range(width):

        scale_factor = width / 5
        x_offset = width / 1.6
        y_offset = height / 2

        x_coord = (x-x_offset) / scale_factor
        y_coord = (y-y_offset) / scale_factor

        point = complex(-0.5, 0.8)
        test_value = complex(x_coord, y_coord)

        for num_iterations in range(iterations):
            test_value = test_value ** 2 + point
            #test_value = complex(abs(test_value.real), abs(test_value.imag)) ** 2 + point

            if (abs(test_value) > 5):
                pixels[x, height - y - 1] = get_color(num_iterations)
                break
        else:
            pixels[x, height - y - 1] = background


img = img.convert("RGB")

resolution = str(width) + 'x' + str(height)
time = str(datetime.now().strftime('%Y.%m.%d %H.%M.%S'))
filename = 'mandelbrot' + ' ' + resolution + ' ' + time + '.png'
path = os.path.join(os.path.dirname(__file__), 'fractal_images', filename)

img.save(path)

img.show()