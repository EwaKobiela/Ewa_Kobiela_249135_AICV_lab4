import cv2
import numpy as np
from random import randrange

def edges(img):
    scale = 1
    delta = 0
    ddepth = cv2.CV_16S
    grad_x = cv2.Sobel(img, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    grad_y = cv2.Sobel(img, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    return grad

# Load images
img1 = cv2.imread(r'lena.png', 0)
img2 = cv2.imread(r'lowfreq.png', 0)

# Selecting image to perform operations at:
img = img2.copy()
# OR
#img = img2.copy()
img = np.uint8(img)
cv2.imshow('Base image', img)

#Edge detection
edgy = edges(img)
cv2.imshow('Detedted edges', edgy)

cv2.waitKey()
cv2.destroyAllWindows()
