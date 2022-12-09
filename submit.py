# Image Augmentation using Numpy
# https://www.kaggle.com/code/ichigoku/image-augmentation-using-numpy

import numpy as np

image_path = ""
im = Image.open(image_path)
image = np.array(im)

# filipud
new_img = np.flipud(image)

# rotation
new_img = np.rot90(image)

# roll
new_img = np.roll(image, 1, axis=0)
new_img = np.roll(image, 2, axis=1)

