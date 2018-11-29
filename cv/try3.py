#!/usr/bin/python3

import cv2
import numpy as np
from matplotlib import pyplot as plt

print(cv2.__version__)
#img = cv2.imread('gradient.png',0)

img = cv2.imread('/tmp/civic_dashboard.jpg',0)
#img  = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
  # plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.subplot(2,3,i+1),plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
