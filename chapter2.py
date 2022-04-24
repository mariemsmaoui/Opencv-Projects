import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)

img = cv2.imread("resources/lenna.jpg")

imgGray = cv2.cvtColor(img , cv2.COLOR_BGRA2GRAY)
imgblur =cv2.GaussianBlur(imgGray, (7,7),0)#kernel have to be odd numbers
imgCanny= cv2.Canny(img,150,200)
imgDilation=cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded=cv2.erode(imgDilation,kernel,iterations=2)

cv2.imshow("Gray Image ", imgGray)
cv2.imshow("blur Image ", imgblur)
cv2.imshow("Canny Image ", imgCanny)
cv2.imshow("dilation Image ", imgDilation)
cv2.imshow("eroded Image ", imgEroded)


cv2.waitKey(0)