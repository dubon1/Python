#!/usr/bin/python3

import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


#image = mpimg.imread("/tmp/three_companies.jpg")

img = cv2.imread('/tmp/three_companies.jpg')
plt.axis("on")
plt.imshow(img)
plt.show()


