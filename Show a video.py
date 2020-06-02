import cv2

print("package installed")
cap = cv2.VideoCapture("resourecs/Dota 2 2020-03-08 14-35-18.mp4") #add a video file path
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
