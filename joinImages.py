import cv2
import numpy as  np

img=cv2.imread("resources/lenna.jpg")

ImgHor=np.hstack((img,img))
ImgVer=np.vstack((img,img))

cv2.imshow("horizotal",ImgHor)
cv2.imshow("Vaertical",ImgVer)


cv2.waitKey(0)