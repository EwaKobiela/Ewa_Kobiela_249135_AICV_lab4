import cv2
import numpy as np
from random import randrange

def salt(img):
    rows, cols = img.shape[:2]
    #Defining noise density as % of the signal, might be also set to any value
    density = (rows*cols*0.4)//2
    density=int(density)
    print(density)
    for d in range(0,density):
        i = randrange(cols)
        j = randrange(rows)
        img[j,i] = 255
    return img

def pepper(img):
    rows, cols = img.shape[:2]
    #Defining noise density as % of the signal, might be also set to any value
    density = (rows * cols * 0.4) // 2
    density = int(density)
    for d in range(0,density):
        i = randrange(cols)
        j = randrange(rows)
        img[j,i] = 0
    return img

def noise(img):
    s = salt(img)
    p = pepper(img)
    noise = cv2.addWeighted(s, 0.5, p, 0.5, 0.0)
    out = cv2.addWeighted(img, 0.5, noise, 0.5, 0.0)
    return out

def median_filter(img):
    blur = cv2.medianBlur(img,5)
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
img = img1.copy()
# OR
#img = img2.copy()
img = np.uint8(img)
cv2.imshow('Base image', img)

# Adding S&P noise to image
img_noisy = noise(img)
cv2.imshow('Noisy image', img_noisy)

#Removing noise
img_filter = median_filter(img)
cv2.imshow('Image after median filtering', img_filter)

#Sharpening the picture
img_sharp = sharpen(img_filter)
cv2.imshow('Sharpened image', img_sharp)

cv2.waitKey()
cv2.destroyAllWindows()
