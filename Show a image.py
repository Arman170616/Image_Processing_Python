import cv2

print("show a Image")


img = cv2.imread("resourecs/fortnite-4129124_1920.jpg")  #set a file which consists image
cv2.imshow("output", img)
cv2.waitKey(0)

