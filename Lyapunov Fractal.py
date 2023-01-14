from PIL import Image
import math
import colorsys
import os
from datetime import datetime


resolution = (1000, 1000)

background = (0, 0, 0)
foreground = (255, 255, 255)

img = Image.new('RGB', resolution, background)
pixels = img.load()

iterations = 5


def get_color(exponent):
    normalized = math.log(abs(exponent) + 1)
    if normalized < 0:
        normalized = 0
    elif normalized > 1:
        normalized = 1

    h = .6
    s = .9
    v = normalized

    rgb = colorsys.hsv_to_rgb(h, s, v)

    return (round(rgb[0] * 255), round(rgb[1] * 255), round(rgb[2] * 255))


def generate_fractal(width, height, seed):
    seed = seed * iterations

    scale_factor = width / 4
    x_offset = width * 0
    y_offset = height * 0

    for y in range(height):

        print(round((y / height) * 100, 2), "%")

        for x in range(width):
            a = (x + x_offset) / scale_factor
            b = (y + y_offset) / scale_factor

            test_value = 0
            previous_value = 0.5

            exponent = 0

            for n in range(iterations):
                r = 0
                if seed[n] == "A":
                    r = a
                elif seed[n] == "B":
                    r = b

                test_value = r * previous_value * (1 - previous_value)
                previous_value = test_value

                if n > 1 and x > 0 and y > 0 and previous_value < 0.5:
                    exponent += math.log(abs(r * (1 - (2 * previous_value))))

            exponent = exponent / iterations

            pixels[x, height - y - 1] = get_color(exponent)
        

generate_fractal(img.width, img.height, "BA")

resolution = str(resolution[0]) + 'x' + str(resolution[1])
time = str(datetime.now().strftime('%Y.%m.%d %H.%M.%S'))
filename = 'roots' + ' ' + resolution + ' ' + time + '.png'
path = os.path.join(os.path.dirname(__file__), 'fractal_images', filename)

img.save(path)

img.show()