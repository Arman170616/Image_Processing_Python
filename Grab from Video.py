import cv2
import numpy as np

#need image,video
cap = cv2.VideoCapture(0)
imgTarget = cv2.imread('resourecs/car.jpg')
myVid = cv2.VideoCapture('resourecs/demo.mp4')

success, imgVideo = myVid.read()  # Grab from video
ht, wt, ct = imgTarget.shape        # both shape same
imgVideo = cv2.resize(imgVideo, (wt, ht))  #resize image

cv2.imshow('ImgTarget', imgTarget)
cv2.imshow('myVid', imgVideo)

cv2.waitKey(0)
