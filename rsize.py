import cv2
import numpy as np

img =cv2.imread("resources/lambergini.png")
print(img.shape)


imgResize =cv2.resize(img,(600,310))
print(imgResize.shape)

imgCropped=img[:200,200:700]
cv2.imshow("image",img)
cv2.imshow("image_resized",imgResize)
cv2.imshow("image_Cropped",imgCropped)

cv2.waitKey(0)