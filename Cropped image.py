import cv2
import numpy as np

img = cv2.imread("resourecs/image.jpg")
print(img.shape)

imgCropped = img[100:300, 300:500]
print(imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
