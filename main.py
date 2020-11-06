import numpy as np
from math import floor
from PIL import Image as im

gray_levels = "$@%&*+~=-:. "  # 10 levels of gray is in my opinion sufficient

################
# image loading
################
image = im.open("face.png").convert("L")
width, height = image.size[0], image.size[1]
image_data = np.array(image)

########################
# split image into grid
########################
ascii_cols = 205  # generally the bigger the number, the better
# default courier font scale
font_scale = 0.43
tile_width = round(width / ascii_cols)
tile_height = round(tile_width / font_scale)
ascii_rows = int(height / tile_height)
if not (tile_width % 2):
    tile_width -= 1
if not (tile_height % 2):
    tile_height -= 1


def calculate_average_brightness(img_data, center_x, center_y, wid, hei):
    summ = 0
    divider = wid * hei
    # iterate over the selected image window and calculate average brightness
    for w in range(int(center_x - floor(wid / 2)), int(center_x + floor(wid / 2))):
        for k in range(int(center_y - floor(hei / 2)), int(center_y + floor(hei / 2))):
            summ += img_data[k][w]
    return summ / divider


output_array = [[" " for col in range(ascii_cols)] for row in range(ascii_rows)]

################
# main function
################
for row in range(0, ascii_rows):
    for col in range(0, ascii_cols):
        brightness = calculate_average_brightness(
            image_data,
            floor(tile_width / 2) + col * tile_width,
            floor(tile_height / 2) + row * tile_height,
            tile_width,
            tile_height,
        )
        output_array[row][col] = gray_levels[
            int(round((255 - brightness) / (255 / (len(gray_levels) - 1))))
        ]

for row in range(ascii_rows):
    print("".join(output_array[row]))
