import cv2
import numpy as np
img=cv2.imread("student.jpg")
height=img.shape[0]
width=img.shape[1]
q_height,q_width=height/6,width/4
T = np.float32([[1,0,q_width],[0,1,q_height]])
translate=cv2.warpAffine(img,T,(width,height))
cv2.imshow("image trans",translate)
cv2.waitKey(0)
cv2.destroyAllWindows()#{[1,0,tx][0,1,ty][0,0,1]}