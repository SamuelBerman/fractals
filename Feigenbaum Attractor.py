from PIL import Image
from datetime import datetime
import os


iterations = 1000

width = 7680
height = 4320

background = (20, 20, 20)
foreground = (255, 255, 255)

img = Image.new('RGB', (width, height), background)
pixels = img.load()


for x in range(width):
    scale_factor = width / 1.5
    x_offset = width * 1.65
    y_offset = height *1.15

    x_coord = (x + x_offset) / scale_factor

    test_value = 0.5
    previous_value = 0.5

    for num_iterations in range(iterations):
        test_value = x_coord * previous_value * (1 - previous_value)
        previous_value = test_value

        y = 1-(test_value * scale_factor - y_offset)

        if num_iterations > 500:
            if y > height - 1:
                y = height - 1
            elif y < 0:
                y = 0

            pixels[x, y] = foreground
        

resolution = str(width) + 'x' + str(height)
time = str(datetime.now().strftime('%Y.%m.%d %H.%M.%S'))
filename = 'feigenbaum' + ' ' + resolution + ' ' + time + '.png'
path = os.path.join(os.path.dirname(__file__), 'fractal_images', filename)

img.save(path)

img.show()