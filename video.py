import cv2
cap =cv2.VideoCapture("resources/Bee Gees - How Deep Is Your Love (Official Video).mp4")


while True:
    success,img=cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):#delay and q letter will break the loop
        break
