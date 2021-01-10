import cv2
import numpy as np
from random import randrange

def edges1(img):
    kernel_sharpening = np.array([[0, -1, 0],
                                  [-1, 4, -1],
                                  [0, -1, 0]])
    edges = cv2.filter2D(img, -1, kernel_sharpening)
    return edges

def edges2(img):
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 8, -1],
                                  [-1, -1, -1]])
    edges = cv2.filter2D(img, -1, kernel_sharpening)
    return edges

def edges_sobel(img):
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

#Edge detection
edgy1 = edges1(img)
cv2.imshow('Laplace filter with first kernel', edgy1)
edgy2 = edges2(img)
cv2.imshow('Laplace filter with second kernel', edgy2)
edgy_s = edges_sobel(img)
cv2.imshow('Ready sobel filter', edgy_s)

cv2.waitKey()
cv2.destroyAllWindows()
