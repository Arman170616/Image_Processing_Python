import cv2

print("package installed")

'''
img = cv2.imread("resourecs/fortnite-4129124_1920.jpg")
cv2.imshow("output", img)
cv2.waitKey(0)
'''

#cap = cv2.VideoCapture("resourecs/Dota 2 2020-03-08 14-35-18.mp4")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break