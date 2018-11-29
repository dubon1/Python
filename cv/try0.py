#!/usr/bin/python3

import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


image = mpimg.imread("/tmp/three_companies.jpg")
plt.axis("off")
plt.imshow(image)
#plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))   # color got smashed
plt.show()
