import cv2

import numpy as np

img=np.zeros((512,512,3),np.uint8)
#color images
#print(img)
#img[:]=255,0,0

#img[200:300,100:300]=255,0,0

#create lines
cv2.line(img,(0,0),(img.shape[0],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),70,(255,255,0),4)
#create texts
cv2.putText(img,"open cv",(300,200),cv2.FONT_HERSHEY_PLAIN,2,(0,100,0),2)

cv2.imshow("image",img)

cv2.waitKey(0)