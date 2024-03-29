import cv2
import numpy as np
img=cv2.imread("resources/cards.jpg")

pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])


width, height = 250,350
pts2 = np.float32([[111,219],[287,188],[154,482],[352,440]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("image",img)
cv2.imshow("imgOutput",imgOutput)

cv2.waitKey(0)