import cv2
import numpy as np

def noise(img):
    mean = 0
    stddev = 4
    gauss_noise = np.zeros(img.shape)
    n = cv2.randn(gauss_noise, mean, stddev)
    gauss_noise = np.uint8(gauss_noise)
    out = cv2.addWeighted(img, 0.5, gauss_noise, 0.5, 0.0)
    return out

def gaussian_filter(img):
    blur = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
    return blur

def sharpen(img):
    kernel_sharpening = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened = cv2.filter2D(img, -1, kernel_sharpening)
    return sharpened

# Load images
img1 = cv2.imread(r'lena.png', 0)
img2 = cv2.imread(r'lowfreq.png', 0)

# Selecting image to perform operations at:
img = img2.copy()
# OR
#img = img2.copy()
img = np.uint8(img)
cv2.imshow('Base image', img)

# Adding Gaussian noise to image
img_noisy = noise(img)
cv2.imshow('Noisy image', img_noisy)

#Removing noise
img_filter = gaussian_filter(img)
cv2.imshow('Image after Gaussian filtering', img_filter)

#Sharpening the picture
img_sharp = sharpen(img_filter)
cv2.imshow('Sharpened image', img_sharp)

cv2.waitKey()
cv2.destroyAllWindows()
