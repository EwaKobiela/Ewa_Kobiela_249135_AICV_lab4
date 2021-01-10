import cv2
import numpy as np
from random import randrange

def noise(img):
    mean = 0
    stddev = 4
    gauss_noise = np.zeros(img.shape)
    n = cv2.randn(gauss_noise, mean, stddev)
    gauss_noise = np.uint8(gauss_noise)
    out = cv2.addWeighted(img, 0.5, gauss_noise, 0.5, 0.0)
    return out

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

# Load image
img = cv2.imread(r'lena.png', 0)
img = np.uint8(img)
cv2.imshow('Base image', img)

#Adding Gaussian noise
img_noisy = noise(img)
cv2.imshow('Noisy image', img_noisy)

#Edge detection
edgy = edges(img_noisy)
cv2.imshow('Detected edges', edgy)

cv2.waitKey()
cv2.destroyAllWindows()
